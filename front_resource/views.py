from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book_Resoure,Learn_Resource,Teach_Video,Researcher,Researcher_source
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_page #在视图函数中使用,将视图结果存入缓存
# Create your views here.
#文献资料
#@cache_page(300) #5分钟
def Book_Resource(request):
    page_num = request.GET.get('page',1)
    bookresource = Book_Resoure.objects.all()
    all_data = bookresource
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/resource.html',context)

def Book_Resource_detail(request):
    id =request.GET.get('id',1)
    try:
        bookresource = Book_Resoure.objects.get(id=id)
        next_bookresource = Book_Resoure.objects.filter(id__gt=id).first()
        last_bookresource = Book_Resoure.objects.filter(id__lt=id).last()
    except Exception as e:
        return HttpResponse('报错')
    context = {'bookresource':bookresource,'next_bookresource':next_bookresource,'last_bookresource':last_bookresource}
    return render(request,'front/tDetail1.html',context)

#学习资料
#@cache_page(300) #5分钟
def Learn_Resoure(request):
    page_num = request.GET.get('page', 1)
    learnresource = Learn_Resource.objects.all()
    all_data = learnresource
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/LearnResource.html',context)

#学习资料详情页
def Learn_Resource_Deatil(request):
    id = request.GET.get('id', 1)
    try:
        learnresource = Learn_Resource.objects.get(id=id)
        next_learnresource = Learn_Resource.objects.filter(id__gt=id).first()
        last_learnresource = Learn_Resource.objects.filter(id__lt=id).last()
    except Exception as e:
        return render(request,'front/fail_to_access.html')
    context = {'learnresource': learnresource, 'next_learnresource': next_learnresource,
               'last_learnresource': last_learnresource}
    return render(request, 'front/tcDetail2.html', context)

#@cache_page(300) #5分钟
def Teachvideo(request):
    videos = Teach_Video.objects.all()
    context = {'videos':videos}
    return render(request,'front/resource1.html',context)

def Researcher1(request):
    resources = Researcher_source.objects.all()
    page_num = request.GET.get('page', 1)
    all_data = resources
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/teachers.html',context)

#@cache_page(300) #5分钟
def Researcher_Resource1(request):
    name = request.GET.get('name', '马皇后')
    try:
        researcher = Researcher_source.objects.get(name=name)
        next_researcher = Researcher_source.objects.filter(name__gt=name).first()
        last_researcher = Researcher_source.objects.filter(name__lt=name).last()
    except Exception as e:
        return render(request, 'front/fail_to_access.html')
    context = {'researcher': researcher, 'next_researcher': next_researcher,
               'last_researcher': last_researcher}
    return render(request,'front/researcher_resource.html',context)

def Researcher_Detail(request):
    teacher = Researcher.objects.all()
    page_num = request.GET.get('page', 1)
    all_data = teacher
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/teachers1.html',context)

#@cache_page(300) #5分钟
def Researcher_Include(request):
    name = request.GET.get('name','马老师')
    try:
        researcher = Researcher.objects.get(name=name)
        next_researcher = Researcher.objects.filter(name__gt=name).first()
        last_researcher = Researcher.objects.filter(name__lt=name).last()
    except Exception as e:
        return render(request, 'front/fail_to_access.html')
    context = {'researcher': researcher, 'next_researcher': next_researcher,
               'last_researcher': last_researcher}
    return render(request,'front/teacher_detail.html',context)