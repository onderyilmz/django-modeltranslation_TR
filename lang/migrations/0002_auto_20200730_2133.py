# Generated by Django 2.2.13 on 2020-07-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='content_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='content_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title_de',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title_en',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
