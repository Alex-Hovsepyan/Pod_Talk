# Generated by Django 4.1.7 on 2023-03-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_lastestepisode_general_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastestepisode',
            name='general_title',
        ),
        migrations.RemoveField(
            model_name='trendingepisode',
            name='general_title',
        ),
        migrations.AddField(
            model_name='title',
            name='latest_title',
            field=models.CharField(default=1, max_length=30, verbose_name='Latest Episode General Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='trending_title',
            field=models.CharField(default=1, max_length=30, verbose_name='Trending Episode General Title'),
            preserve_default=False,
        ),
    ]