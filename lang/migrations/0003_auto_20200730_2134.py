# Generated by Django 2.2.13 on 2020-07-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0002_auto_20200730_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='content_tr',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title_tr',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
