# Generated by Django 4.0.2 on 2022-12-14 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_ipmodel_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
    ]
