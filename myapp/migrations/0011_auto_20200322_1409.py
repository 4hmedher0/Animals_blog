# Generated by Django 3.0.4 on 2020-03-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200322_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='img',
            field=models.ImageField(blank=True, default='404.png', upload_to='D:\\project\\media\\.media\\media'),
        ),
    ]