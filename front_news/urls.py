#新闻公告
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('News_index',views.News_index,name="front_news_index"), #新闻公告
    path('News_detail',views.News_detail,name="front_news_detail"),#新闻详情
    path('Work_Dynamic',views.Work_Dynamic,name="front_work_dynamic"),#工作动态
    path('work_dynamic_detail',views.Work_Dynamic_Detail,name="front_work_dynamic_detail"),#工作动态详情页
]