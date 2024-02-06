from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Book_Resoure(models.Model):
    publisher = models.CharField('发布者',max_length=30,default="空空如也")
    title = models.TextField('文献标题',default="空空如也")
    content = HTMLField('文献内容',default="空空如也")
    create_time = models.DateTimeField('发布时间',auto_now_add=True)


    class Meta:
        verbose_name_plural = "文献资源"

    def __str__(self):
        return '%s'%(self.title)
#学习资料
class Learn_Resource(models.Model):
    publisher = models.CharField('发布者', max_length=30, default="空空如也")
    title = models.TextField('资料标题', default="空空如也")
    content = HTMLField('资料内容', default="空空如也")
    create_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = "学习资料"

    def __str__(self):
        return '%s'%(self.title)
#教学视频
class Teach_Video(models.Model):
    image = models.ImageField('封面图片')
    title = models.TextField('视频标题',null=False)
    video = models.FileField(upload_to="front/video")
    create_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = "教学视频"
        #model = Learn_Resource
        #fields = ('title') #从其他模型类中拿，不用自己在定义一遍了

    def __str__(self):
        return '%s'%(self.title)
#专家介绍
class Researcher(models.Model):
    avatar = models.ImageField("专家头像",null=False)
    name = models.CharField('专家名字',max_length=30,primary_key=True)
    content = models.TextField(default="专家介绍")
    create_time = models.DateTimeField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = "研究人员"

    def __str__(self):
        return '%s'%(self.name)
#专家资源
class Researcher_source(models.Model):
    name = models.CharField("专家名字",max_length=30,primary_key=True)
    title = models.TextField('论文标题')
    content = models.TextField("论文内容")
    create_time = models.DateTimeField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = "专家资源"

    def __str__(self):
        return '%s'%(self.name)