# Generated by Django 3.0.6 on 2020-05-24 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_auto_20200328_2201"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ordercartitem",
            options={
                "verbose_name": "Order Item",
                "verbose_name_plural": "Order Items",
            },
        ),
        migrations.RemoveField(model_name="ordercart", name="products",),
        migrations.AddField(
            model_name="ordercartitem",
            name="order_cart",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ordercartitem_ordercart",
                to="shop.OrderCart",
                verbose_name="Order Cart",
            ),
        ),
    ]