# coding=utf-8
import json

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Topic,Comments
import hashlib
from tools.check_login import check_login
from django.views.decorators.cache import cache_page #在视图函数中使用,将视图结果存入缓存
from django.core import mail
from django.db.models import Count, Q
from front_news.models import News,Work
from front_researchGain.models import Projects
from front.models import Topic
from front_resource.models import Teach_Video,Researcher,Researcher_source,Book_Resoure,Learn_Resource
from django.db import models
import os
from django.conf import settings
# Create your views here.
#前端平台个人列表页数据
def make_topics_res(username,topics,page_num):
    res={}
    topic_res = []
    for topic in topics:
        d = {}
        d['title'] = topic.topic_title
        d['sumary'] = topic.sumary
        d['comment_number'] = topic.comment_number
        d['username'] = username
        d['create_time'] = topic.create_time
        d['id'] = topic.id
        topic_res.append(d)
    res['topics'] = topic_res

    all_data = topic_res
    # 初始化paginator
    paginator = Paginator(all_data, 4)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))

    res['c_page'] = c_page
    res['paginator'] = paginator
    return res

#前端平台首页
def index(request):
    try:
        second_news = News.objects.all().order_by("-create_time")[1:3] #拿最晚发布的第二个和第三个新闻
        last_news = News.objects.all().last()
        second_works = Work.objects.all().order_by("-create_time")[1:3]##拿最晚发布的第二个和第三个工作动态
        last_works = Work.objects.all().last()
        works = Work.objects.all()
        projects = Projects.objects.all()
        topics = Topic.objects.all()
        video = Teach_Video.objects.all()
        researcher = Researcher.objects.all()
        researcher_resource = Researcher_source.objects.all()
        book_resource = Book_Resoure.objects.all()
        learn_resource = Learn_Resource.objects.all()
    except Exception as e:
        return render(request, 'front/fail_to_access.html')
    context = {'last_news':last_news,'second_news':second_news,'second_works':second_works,'last_works':last_works,'works':works,
               'projects':projects,'topics':topics,'video':video,'researcher':researcher,'researcher_resource':researcher_resource,
               'book_resource':book_resource,'learn_resource':learn_resource}
    return render(request,'front/index.html',context)
#前端平台登录
def login(request):
    if request.method == 'GET':
        # 检查登录状态,如果登录了,显示'已登录'
        #检查session
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('/')  #302跳转 重定向
            #return redirect(reverse("front_login")) 这样也行
        #检查cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            #回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return HttpResponseRedirect('/')  # 302跳转 重定向

        return render(request,'front/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #json_str = request.body
        #json_obj = json.loads(json_str)
        #username = json_obj['username']
        #password = json_obj['password']
        #print(username,password)
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('用户名或密码错误')
        #比对密码
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')
        #记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id #主键

        resp =  HttpResponseRedirect('/')  # 302跳转 重定向

        #判断用户是否点选了'记住用户名'
        if 'remember' in request.POST:
            username = username.encode("utf-8")
            resp.set_cookie('username',username,3600*24) #存一天,不设置默认关闭浏览器失效
            resp.set_cookie('uid',user.id,3600*24) #存一天   #使用这个需要response对象

        return resp


#前端平台注册
def register(request):
    if request.method == 'GET':
        return render(request,'front/re.html')

    if request.method == 'POST':
        #POST提交数据
        username = request.POST['username'] #表单提交要通过这个来获取
        password = request.POST['password']
        password_check = request.POST['password_check']
        if password != password_check:
            return HttpResponse('两次输入密码不一致')
        old_users = User.objects.filter(username=username) #条件查询 Django shell(用于操作模型层的工具)
        if old_users:
            return HttpResponse('用户名已注册')
        m = hashlib.md5() #生成md5的计算对象
        m.update(password.encode()) #类型为字节串
        password_m = m.hexdigest()
        try:
           user = User.objects.create(username=username,password=password_m)
        except Exception as e:
            print('注册失败 %s'%(e))
            return HttpResponse('用户名已注册')
        #登录保持
        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponseRedirect('/')

#前端平台退出登录
def quit(request):
    resp = HttpResponseRedirect('/')
    try:
        if request.session['username']:
            del request.session['username']
        if request.session['uid']:
            del request.session['uid']
        if request.COOKIES['username']:
            resp.delete_cookie('username')
        if request.COOKIES['uid']:
            resp.delete_cookie('uid')
    except Exception as e:
        print(e)


    return resp

#前端平台个人中心
#校验登录状态
@check_login
def personal_center(request):
    if request.method == 'GET':
        username = request.session['username']
        try:
            user = User.objects.get(username=username)
            nickname = user.nickname
            email = user.email
            info = user.info
            context = {'username':username,'nickname':nickname,'email':email,'info':info}
            return render(request,'front/personal.html',context)
        except Exception as e:
            return HttpResponseRedirect('/login')

    if request.method == 'POST':
        #纯python的上传方式
        #a_file = request.FILES['myfiles']
        #print('上传的文件是:',a_file.name)
        #filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        #with open(filename,'wb') as f:
            #data = a_file.file.read()
            #f.write(data)
        avatar = request.POST['avatar']
        info = request.POST['info']
        username = request.POST['username']
        nickname = request.POST['nickname']
        email = request.POST['email']
        print(email)
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponseRedirect('/login')
        user.avatar = avatar
        user.info = info
        user.nickname = nickname
        user.email = email
        user.save()
        #mail.send_mail(subject="计算机中心", message="恭喜你修改信息成功",from_email='xxxxxxxx@qq.com',recipient_list=['xxxxxxxxxxxxxxxxx@163.com'])#修改信息后发送邮件
        return HttpResponseRedirect('/')

#@cache_page(300) #存5分钟
@check_login
def topic(request):
    if request.method == 'GET':
        #/mytopic?page=1 采用查询字符串的方式 利用Paginator
        id = request.session['uid']
        topics = Topic.objects.filter(userID_id=id)
        user = User.objects.get(id=id)
        page_num = request.GET.get('page', 1)
        res = make_topics_res(user.username,topics,page_num)

    return render(request,'front/ownTopic.html',res)

#话题详情
def Topic_detail(request):
    if request.method == 'GET':
        topic_id = request.GET.get('id',9)
        try:
            topic = Topic.objects.get(id=topic_id)
            user = User.objects.get(id=topic.userID_id)
            username = request.session['username']
            publisher = User.objects.get(username = username)
            #评论
            first_content = Comments.objects.filter(topicID_id=topic.id,parent_comment_ID=0)
            #回复
            second_content = Comments.objects.filter(topicID_id=topic.id,parent_comment_ID__gt=0)
            #对评论进行计数
            first_num = Comments.objects.filter(topicID_id=topic.id, parent_comment_ID=0).aggregate(
                Count('comment_content'))
            #对回复数计数(分组查询)
            res = Comments.objects.filter(topicID_id=topic.id,parent_comment_ID__gt=0).values('parent_comment_ID').order_by().annotate(Count('parent_comment_ID'))
            #res=(res)
            #对排名进行查询
            topic_or = Topic.objects.values('userID_id').annotate(c=Count('comment_number')).order_by()
            #print(topic_or)
            order = []
            for h in topic_or:
                d = {}
                user = User.objects.get(id=h['userID_id'])
                d['username'] = user.username
                d['avatar'] = user.avatar
                d['comment_number'] = h['c']
                order.append(d)
            print(order)

            context = {'username':user.username,'title':topic.topic_title,'content':topic.topic_content,'date':topic.create_time,'topic_id':topic.id,'publisher':publisher,'first_content':first_content,
                       'second_content':second_content,'first_num':first_num,'res':res,'order':order}
            #print(context)
            topic.comment_number = int(first_num['comment_content__count'])
            topic.save()
            # 对回复进行计数
        except Exception as e:
            return HttpResponseRedirect('/login')
        return render(request,'front/tDetail.html',context)

    if request.method == 'POST':
        topic_id = request.GET.get('id',9)
        publisher = request.session['username']
        topic = Topic.objects.get(id=topic_id)
        user =User.objects.get(username=publisher)
        try:
            content = request.POST['content']
            parent_id = request.GET.get('parent_id','错误')
            Comments.objects.create(comment_content=content,topicID_id=topic.id,userID_id=topic.userID_id,publisher=publisher,avatar=user.avatar,parent_comment_ID=parent_id)
            return HttpResponseRedirect('/Topic_detail?id='+topic_id)
        except Exception as e:
            content = request.POST['tinymce']
            Comments.objects.create(comment_content=content,topicID_id=topic.id,userID_id=topic.userID_id,publisher=publisher,avatar=user.avatar)
            return HttpResponseRedirect('/Topic_detail?id='+topic_id)



#话题编辑
@check_login
def Topic_edit(request):
    if request.method == 'GET':
        return render(request,'front/public.html')
    if request.method == 'POST':
        topic_title = request.POST['title']
        topic_content = request.POST['tinymce']
        sumary =topic_content[:60]
        user = User.objects.get(username=request.session['username'])
        Topic.objects.create(topic_title=topic_title,topic_content=topic_content,sumary=sumary,userID_id=user.id)
        return HttpResponseRedirect('/myTopic')

#前端平台－中心论坛
def Center_forum(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        page_num = request.GET.get('page', 1)
        all_data = topics
        # 初始化paginator
        paginator = Paginator(all_data, 7)  # 每一页显示４条数据
        # 初始化对应页码的page对象
        c_page = paginator.page(int(page_num))
        for t in c_page:
            user = User.objects.get(id=t.userID_id)
            #t['username'] = user.username
            t.username = user.username
        # 对排名进行查询
        topic_or = Topic.objects.values('userID_id').annotate(c=Count('comment_number')).order_by()
        # print(topic_or)
        order = []
        for h in topic_or:
            d = {}
            user = User.objects.get(id=h['userID_id'])
            d['username'] = user.username
            d['avatar'] = user.avatar
            d['comment_number'] = h['c']
            order.append(d)
            #print(order)
        context = {'topics':topics,'c_page':c_page,'paginator':paginator,'order':order}
        return render(request,'front/topic.html',context)
    if request.method == 'POST':
        search_text = request.POST['search_text']
        topics = Topic.objects.filter(Q(topic_title__icontains=search_text)|Q(topic_content__icontains=search_text))
        print(topics)
        page_num = request.GET.get('page', 1)
        all_data = topics
        # 初始化paginator
        paginator = Paginator(all_data, 7)  # 每一页显示４条数据
        # 初始化对应页码的page对象
        c_page = paginator.page(int(page_num))
        for t in c_page:
            user = User.objects.get(id=t.userID_id)
            # t['username'] = user.username
            t.username = user.username
        # 对排名进行查询
        topic_or = Topic.objects.values('userID_id').annotate(c=Count('comment_number')).order_by()
        # print(topic_or)
        order = []
        for h in topic_or:
            d = {}
            user = User.objects.get(id=h['userID_id'])
            d['username'] = user.username
            d['avatar'] = user.avatar
            d['comment_number'] = h['c']
            order.append(d)
           # print(order)
        context = {'topics': topics, 'c_page': c_page, 'paginator': paginator, 'order': order}
        return render(request, 'front/topic.html', context)



#中心概况
def Center_profile(request):

    if request.method == 'GET':
        return render(request,'front/about.html')

