# Generated by Django 3.0.2 on 2020-03-28 16:33

from django.db import migrations, models
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_add_update_at_order"),
    ]

    operations = [
        migrations.RemoveField(model_name="productphoto", name="photo",),
        migrations.RemoveField(model_name="productphoto", name="photo_alt",),
        migrations.AddField(
            model_name="productphoto",
            name="image_alt",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Images Alt"
            ),
        ),
        migrations.AddField(
            model_name="productphoto",
            name="image_preview",
            field=optimized_image.fields.OptimizedImageField(
                blank=True, upload_to="", verbose_name="Images"
            ),
        ),
    ]