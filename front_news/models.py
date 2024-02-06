from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class News(models.Model):
    image = models.ImageField('首页图片')
    title = models.TextField('新闻标题',default="空空如也")
    content = HTMLField('新闻',default='空空如也')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = '新闻管理'

    def __str__(self):

        return '%s'%(self.title)

class Work(models.Model):
    image = models.ImageField('首页图片')
    title = models.TextField('工作标题',default="空空如也")
    content = HTMLField('工作内容',default='空空如也')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = '工作动态'

    def __str__(self):

        return '%s'%(self.title)

