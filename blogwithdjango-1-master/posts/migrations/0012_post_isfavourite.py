# Generated by Django 4.0.2 on 2022-12-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isfavourite',
            field=models.BooleanField(default=False),
        ),
    ]