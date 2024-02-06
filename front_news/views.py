from django.shortcuts import render
from .models import News,Work
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views.decorators.cache import cache_page #在视图函数中使用,将视图结果存入缓存
#@cache_page(300) #存５分钟
def News_index(request):
    page_num = request.GET.get('page',1)
    news = News.objects.all()
    all_data = news
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page':c_page,'paginator':paginator}
    return render(request,'front/news.html',context)

def News_detail(request):
    id = request.GET.get('id',1)
    try:
        news = News.objects.get(id=id)
        next_news = News.objects.filter(id__gt=id).first()
        last_news = News.objects.filter(id__lt=id).last()
    except Exception as e:
        return HttpResponseRedirect('/News/News_index')
    context = {'news':news,'next_news':next_news,'last_news':last_news}
    return render(request,'front/nDetail.html',context)


def Work_Dynamic(request):
    page_num = request.GET.get('page', 1)
    works = Work.objects.all()
    all_data = works
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示４条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/work.html',context)

def Work_Dynamic_Detail(request):
    id = request.GET.get('id', 1)
    try:
        works = Work.objects.get(id=id)
        next_works = Work.objects.filter(id__gt=id).first()
        last_works = Work.objects.filter(id__lt=id).last()
    except Exception as e:
        return HttpResponseRedirect('报错')
    context = {'works': works, 'next_works': next_works, 'last_works': last_works}
    return render(request, 'front/Work_Dynamic.html', context)