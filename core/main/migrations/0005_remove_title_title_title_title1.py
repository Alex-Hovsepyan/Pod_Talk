# Generated by Django 4.1.7 on 2023-03-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_title_title5_alter_title_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='title',
        ),
        migrations.AddField(
            model_name='title',
            name='title1',
            field=models.CharField(default=1, max_length=40, verbose_name='Title-1'),
            preserve_default=False,
        ),
    ]
