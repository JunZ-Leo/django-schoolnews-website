# Generated by Django 2.2.12 on 2022-06-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_auto_20220623_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='avatar',
            field=models.TextField(default='空空如也', verbose_name='评论者头像'),
        ),
    ]
