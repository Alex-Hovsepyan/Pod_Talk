# Generated by Django 4.1.7 on 2023-03-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_subtitle1_footer_subtitle_alter_footer_li4'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderNavbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=20, verbose_name='Title-1')),
            ],
        ),
        migrations.RemoveField(
            model_name='header',
            name='subtitle1',
        ),
        migrations.RemoveField(
            model_name='header',
            name='subtitle2',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title3',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title4',
        ),
    ]