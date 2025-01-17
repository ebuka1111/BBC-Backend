# Generated by Django 4.2.7 on 2023-11-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
