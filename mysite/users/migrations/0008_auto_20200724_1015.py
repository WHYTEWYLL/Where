# Generated by Django 3.0.8 on 2020-07-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200724_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='middlepoint',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
