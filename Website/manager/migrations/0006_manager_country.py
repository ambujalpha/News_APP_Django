# Generated by Django 3.0.3 on 2020-04-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_manager_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='country',
            field=models.TextField(default=''),
        ),
    ]
