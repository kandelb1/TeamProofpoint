# Generated by Django 3.1.2 on 2020-11-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20201103_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='attachment',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='lead',
            name='url',
            field=models.BooleanField(default='False'),
        ),
    ]
