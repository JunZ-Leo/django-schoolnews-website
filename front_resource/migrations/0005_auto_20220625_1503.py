# Generated by Django 2.2.12 on 2022-06-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_resource', '0004_teach_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teach_video',
            options={'verbose_name': '教学视频'},
        ),
        migrations.AlterField(
            model_name='teach_video',
            name='video',
            field=models.FileField(upload_to='media/front/video'),
        ),
    ]
