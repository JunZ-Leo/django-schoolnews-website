from django.contrib import admin
from .models import Book_Resoure,Learn_Resource,Teach_Video,Researcher,Researcher_source
# Register your models here.

#模型管理器类
class Book_ResoureManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','publisher','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Book_Resoure,Book_ResoureManager) #绑定注册模型管理器和模型类

#模型管理器类
class Learn_ResourceManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','publisher','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Learn_Resource,Learn_ResourceManager) #绑定注册模型管理器和模型类

#模型管理器类
class Teach_VideoManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Teach_Video,Teach_VideoManager) #绑定注册模型管理器和模型类

#模型管理器类
class ResearcherManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['name','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['name'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Researcher,ResearcherManager) #绑定注册模型管理器和模型类

#模型管理器类
class Researcher_sourceManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['name','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['name'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Researcher_source,Researcher_sourceManager) #绑定注册模型管理器和模型类