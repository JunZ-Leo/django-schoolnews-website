#前端子路由文件
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns =[
    path('',views.index,name='front_index'),#首页
    path('login', views.login, name="front_login"),#登录
    path('register',views.register,name="front_register"),#注册
    path('quit',views.quit,name="front_quit"),#退出登录
    path('personal_center',views.personal_center,name="front_personal_center"), #个人中心
    path('myTopic',views.topic,name="front_topic"),
    path('Topic_detail',views.Topic_detail,name="front_topic_detail"),#编辑话题
    path('Topic_edit',views.Topic_edit,name="front_topic_edit"),
    path('Center_forum',views.Center_forum,name="front_center_forum"),#中心论坛
    path('Center_profile',views.Center_profile,name="front_center_profile"),#中心概述
]