from django.contrib import admin
from .models import Projects

# Register your models here.
class ProjectsManager(admin.ModelAdmin):   #添加相应的类属性完成相应的功能
    list_display = ['title','create_time']
    list_filter = ['create_time'] #添加过滤器
    search_fields = ['title'] #添加搜索框[模糊查询]
# Register your models here.
admin.site.register(Projects,ProjectsManager)#绑定注册模型管理器和模型类
