# Generated by Django 2.1 on 2018-11-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_seo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title Seo')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Keywords')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_seo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title Seo')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Keywords')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('image_preview', models.ImageField(blank=True, upload_to='', verbose_name='Images')),
                ('image_alt', models.CharField(blank=True, max_length=255, verbose_name='Images Alt')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='Slug')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('category', models.ManyToManyField(blank=True, related_name='product_categories',
                                                    to='shop.Category', verbose_name='Category')),
                ('tags', models.ManyToManyField(blank=True, related_name='product_tags',
                                                to='tags.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]