from django.contrib import admin
from .models import News,Work
#超级用户可以有多个

#模型管理器类
class NewsManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
    #list_editable = ['title'] #添加可在列表页编辑的字段,要在list_display中出现,与search_fields相互斥
# Register your models here.
admin.site.register(News,NewsManager) #绑定注册模型管理器和模型类

class WorkManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
    #list_editable = ['title'] #添加可在列表页编辑的字段,要在list_display中出现,与search_fields相互斥
# Register your models here.
admin.site.register(Work,WorkManager) #绑定注册模型管理器和模型类
#官网:https://docs.djangoproject.com/en/2.2/ref/contrib/admin/  需要用什么就去里面查
