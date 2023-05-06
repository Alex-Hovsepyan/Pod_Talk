# Generated by Django 4.1.7 on 2023-03-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_topic_rename_lastestepisodes_lastestepisode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Specialist Image')),
                ('name', models.CharField(max_length=20, verbose_name='Specialist Name')),
                ('profession', models.CharField(max_length=70, verbose_name='Specialist Profession')),
                ('symbol_img', models.ImageField(upload_to='images', verbose_name='Specialist Verified')),
                ('social', models.CharField(max_length=60, verbose_name='Specialist Social')),
                ('check_btn', models.BooleanField(verbose_name='YES/NO')),
            ],
        ),
    ]
