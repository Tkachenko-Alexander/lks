# Generated by Django 2.0.6 on 2018-06-06 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-created_at',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='pub_date',
            new_name='created_at',
        ),
    ]
