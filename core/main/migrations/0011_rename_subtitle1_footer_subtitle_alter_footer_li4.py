# Generated by Django 4.1.7 on 2023-03-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_footer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='subtitle1',
            new_name='subtitle',
        ),
        migrations.AlterField(
            model_name='footer',
            name='li4',
            field=models.CharField(max_length=30, verbose_name='Footer li-4'),
        ),
    ]