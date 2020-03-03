# Generated by Django 3.0.2 on 2020-02-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscribe", "0002_subscribe_hidden"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscribe",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email"
            ),
        ),
        migrations.AlterField(
            model_name="subscribe",
            name="hidden",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Hidden"
            ),
        ),
    ]
