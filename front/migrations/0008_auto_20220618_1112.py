# Generated by Django 2.2.12 on 2022-06-18 03:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_auto_20220617_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_content',
            field=tinymce.models.HTMLField(default='空空如也', verbose_name='话题内容'),
        ),
    ]
