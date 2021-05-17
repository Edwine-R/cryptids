# Generated by Django 3.1.7 on 2021-03-25 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptids', '0003_animal_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='Animal',
        ),
        migrations.AddField(
            model_name='animal',
            name='location',
            field=models.ForeignKey(default= 1, on_delete=django.db.models.deletion.CASCADE, to='cryptids.location'),
            preserve_default=False,
        ),
    ]