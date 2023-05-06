# Generated by Django 4.1.7 on 2023-03-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_headernavbar_header_subtitle1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=30, verbose_name='About First Title')),
                ('text1', models.TextField(verbose_name='About First Text')),
                ('text2', models.TextField(verbose_name='About Second Text')),
                ('img', models.ImageField(upload_to='images', verbose_name='About Image')),
                ('title2', models.CharField(max_length=30, verbose_name='About Second Title')),
            ],
        ),
    ]
