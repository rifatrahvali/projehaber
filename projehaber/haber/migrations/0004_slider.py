# Generated by Django 5.0.2 on 2024-04-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0003_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='slider')),
            ],
        ),
    ]
