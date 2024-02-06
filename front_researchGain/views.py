from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect
from .models import Projects
# Create your views here.
from django.views.decorators.cache import cache_page #在视图函数中使用,将视图结果存入缓存

#@cache_page(300) #存５分钟
def ResearchGain_index(request):
    return render(request,'front/course.html')


def Projects_Center(request):
    page_num = request.GET.get('page',1)
    projects = Projects.objects.all()
    all_data = projects
    # 初始化paginator
    paginator = Paginator(all_data, 12)  # 每一页显示12条数据
    # 初始化对应页码的page对象
    c_page = paginator.page(int(page_num))
    context = {'c_page': c_page, 'paginator': paginator}
    return render(request,'front/course1.html',context)

def Projects_detail(request):
    id = request.GET.get('id',1)
    try:
        project = Projects.objects.get(id=id)
    except Exception as e:
        return render(request, 'front/fail_to_access.html')
    context = {'project':project}
    return render(request,'front/tcDetail.html',context)


