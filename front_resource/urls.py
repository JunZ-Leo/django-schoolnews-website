from django.urls import path,include
from . import views

urlpatterns = [
    path('Book_Resource',views.Book_Resource,name="front_book_resource"),#文献资料列表页
    path('Book_Resource_detail',views.Book_Resource_detail,name="front_book_resource_detail"),#文献资料详情页
    path('Learn_Resource',views.Learn_Resoure,name="front_learn_resource"),#学习资料
    path('Learn_Resource_detail',views.Learn_Resource_Deatil,name="front_learn_resource_detail"),#学习资料详情页
    path('Teach_Video',views.Teachvideo,name="front_teach_video"),#教学视频
    path('Researcher',views.Researcher1,name="front_researcher"),#研究人员
    path('Researcher_resource',views.Researcher_Resource1,name="front_researcher_resource"),#专家资源
    path('Researcher_Detail',views.Researcher_Detail,name="front_researcher_detail"),#专家介绍
    path('Researcher_Include',views.Researcher_Include,name="front_researcher_include"),
]