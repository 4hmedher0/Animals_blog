# Generated by Django 3.0.4 on 2020-03-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200317_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]