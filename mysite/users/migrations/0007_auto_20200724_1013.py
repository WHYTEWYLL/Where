# Generated by Django 3.0.8 on 2020-07-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200724_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='middlepoint',
            name='info',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='middlepoint',
            name='middle_points',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
