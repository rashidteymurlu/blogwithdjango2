# Generated by Django 4.0.2 on 2022-12-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_category_tags_remove_post_views_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
