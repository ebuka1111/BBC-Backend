# Generated by Django 4.2.7 on 2023-12-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_date_posted_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='reporter',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
