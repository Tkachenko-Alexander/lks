# Generated by Django 3.0.2 on 2020-01-06 14:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content_en",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                null=True, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content_ru",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                null=True, verbose_name="Content"
            ),
        ),
    ]
