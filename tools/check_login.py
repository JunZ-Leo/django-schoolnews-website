#检查登录状态
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
#装饰器
def check_login(fn):
    #里面是包裹的函数的参数
    def wrap(request,*args,**kwargs):
        #如果登录了就返回到视图函数里
        if 'username' not in request.session or 'uid' not in request.session:
            #检查Cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid') #相比与request.COOKIES['']较为温柔
            if not c_username or not c_uid:
                return HttpResponseRedirect('/login')
            else:
                #回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request,*args,**kwargs)

    return wrap










#基础的装饰器结构
#def check_login(fn):
    # 里面是包裹的函数的参数
    #def wrap(request, *args, **kwargs):
        #return fn(request, *args, **kwargs)

    #return wrap
#装饰器:在包装的环境下调用函数,返回一个修改后的函数对象