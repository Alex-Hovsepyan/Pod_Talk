# Generated by Django 4.1.7 on 2023-03-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_contactpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Footer Title')),
                ('li1', models.CharField(max_length=30, verbose_name='Footer li-1')),
                ('li2', models.CharField(max_length=30, verbose_name='Footer li-2')),
                ('li3', models.CharField(max_length=30, verbose_name='Footer li-3')),
                ('li4', models.CharField(max_length=30, verbose_name='Footer li-1')),
                ('subtitle1', models.CharField(max_length=30, verbose_name='Footer Subtitle')),
                ('social', models.CharField(max_length=25, verbose_name='Footer Social')),
                ('footer_info', models.CharField(max_length=60, verbose_name='Footer Info')),
                ('img1', models.ImageField(upload_to='images', verbose_name='Social Image 1')),
                ('img2', models.ImageField(upload_to='images', verbose_name='Social Image 2')),
            ],
        ),
    ]
