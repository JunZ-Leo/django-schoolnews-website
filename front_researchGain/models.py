from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Projects(models.Model):
    image = models.ImageField('项目图片')
    responsible_person = models.CharField('负责人',max_length=30)
    title = models.TextField('项目标题',default="空空如也")
    content = HTMLField('项目内容',default="空空如也")
    create_time = models.DateTimeField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = "项目"

    def __str__(self):
        return '%s'%(self.title)

