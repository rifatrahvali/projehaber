# Generated by Django 5.0.2 on 2024-04-04 00:23

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0004_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='news')),
                ('context', ckeditor.fields.RichTextField()),
                ('publishDate', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haber.category')),
            ],
        ),
    ]
