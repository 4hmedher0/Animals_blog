# Generated by Django 2.2.2 on 2019-09-19 09:37

from django.db import migrations, models

#from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        #HStoreExtension(),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='empty.png', upload_to='')),
            ],
        ),
    ]
