# Generated by Django 3.0.8 on 2020-07-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200724_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='middlepoint',
            name='info',
        ),
    ]
