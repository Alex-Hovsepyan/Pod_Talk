# Generated by Django 4.1.7 on 2023-03-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_lastestepisodes_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Topic Image')),
                ('title', models.CharField(max_length=20, verbose_name='Topic Title')),
                ('episodes', models.CharField(max_length=25, verbose_name='Topic Episodes')),
            ],
        ),
        migrations.RenameModel(
            old_name='LastestEpisodes',
            new_name='LastestEpisode',
        ),
        migrations.RenameModel(
            old_name='TrendingEpisodes',
            new_name='TrendingEpisode',
        ),
    ]
