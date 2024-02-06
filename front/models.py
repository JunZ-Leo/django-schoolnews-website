from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.
#用户模块
#1.注册 - 成为平台的用户
#(禁止掉crsf[POST提交的403问题])
#2.登陆 - 校验用户身份
#3 退出登录 - 退出登陆状态
#ORM 对象关系映射器 pymysql 本质上会根据对接的数据库引擎,翻译成对应的sql语句

#用户
class User(models.Model):
    username = models.CharField("用户名",max_length=30,unique=True)
    password = models.CharField("密码",max_length=32)
    avatar = models.TextField(null=False)
    nickname = models.CharField('昵称',max_length=50,default="空空如也")
    info = models.CharField('个人签名',max_length=150,default="空空如也")
    email = models.EmailField(default="空空如也")
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('更新时间',auto_now_add=True)

    #表名为应用名_模型类_
    def __str__(self):
        return 'username %s'%(self.username)
    class Meta:
        #verbose_name = '用户管理'
        verbose_name_plural = '用户'
        #db_table = '数据表名'
#话题
class Topic(models.Model):
    topic_title = models.TextField('话题标题',null=False)
    topic_content = HTMLField(verbose_name='话题内容',default="空空如也")
    topic_date = models.DateTimeField('发布时间',auto_now_add=True)
    comment_number = models.IntegerField('评论数量',default=0)
    sumary = models.TextField('摘要信息',default='空空如也')
    create_time = models.DateTimeField('创建时间',default=timezone.now)
    updated_time = models.DateTimeField('更新时间',default=timezone.now)
    total_views = models.IntegerField('浏览量',default=0)
    userID = models.ForeignKey('User',on_delete=models.CASCADE)

    def __str__(self): #object基类的一个方法
        return self.topic_title
    class Meta:
        #db_table = 'Topic' #设置表名
        ordering = ('-create_time',) #排序
        #verbose_name = '话题管理'
        verbose_name_plural = '话题管理'


class Comments(models.Model):
    userID = models.ForeignKey('User',on_delete=models.CASCADE) #
    topicID = models.ForeignKey('Topic',on_delete=models.CASCADE)
    comment_date = models.DateTimeField('评论发布时间',auto_now_add=True)
    comment_content = models.TextField('评论内容',null=False)
    parent_comment_ID = models.IntegerField(null=True,default=0)
    publisher = models.CharField('评论发布者',max_length=30,default='空空如也')
    avatar = models.TextField('评论者头像',default='空空如也')

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '评论管理'


