# Generated by Django 3.1.7 on 2021-03-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptids', '0004_auto_20210325_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
