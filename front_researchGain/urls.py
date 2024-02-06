#研究成果
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Gain_index',views.ResearchGain_index,name="front_researchGain_index"),#专利成果
    path('Projects_Center',views.Projects_Center,name="front_projects_center"),#项目中心
    path('Projects_detail',views.Projects_detail,name="front_projects_detail"),#项目详情页
]

