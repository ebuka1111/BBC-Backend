# Generated by Django 4.2.7 on 2023-11-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('reporter', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
