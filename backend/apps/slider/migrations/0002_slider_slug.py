# Generated by Django 2.1 on 2018-11-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slug',
            field=models.CharField(default='', max_length=120, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
