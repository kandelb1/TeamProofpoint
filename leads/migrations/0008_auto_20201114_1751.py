# Generated by Django 3.1.2 on 2020-11-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20201114_1751'),
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