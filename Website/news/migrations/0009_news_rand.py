# Generated by Django 3.0.3 on 2020-04-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_news_act'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]
