# Generated by Django 2.1 on 2018-12-05 11:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Specification'),
            preserve_default=False,
        ),
    ]