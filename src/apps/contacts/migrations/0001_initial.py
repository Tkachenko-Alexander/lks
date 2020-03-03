# Generated by Django 3.0.2 on 2020-02-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=63, null=True, verbose_name="Name"
                    ),
                ),
                ("message", models.TextField(verbose_name="Message")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        null=True,
                        verbose_name="Phone number",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "company",
                    models.CharField(
                        blank=True, max_length=63, null=True, verbose_name="Company"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
            ],
            options={"verbose_name": "Contact", "verbose_name_plural": "Contacts",},
        ),
    ]
