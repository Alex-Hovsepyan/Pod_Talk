# Generated by Django 4.1.7 on 2023-03-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_lastestepisodes_title_alter_lastestepisodes_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastestepisodes',
            name='title',
            field=models.CharField(max_length=35, verbose_name='Latest Episodes Title'),
        ),
    ]
