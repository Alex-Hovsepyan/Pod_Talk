# Generated by Django 4.1.7 on 2023-03-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_user_img_trendingepisodes_user_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendingepisodes',
            name='check_btn',
            field=models.BooleanField(default=1, verbose_name='YES/NO'),
            preserve_default=False,
        ),
    ]
