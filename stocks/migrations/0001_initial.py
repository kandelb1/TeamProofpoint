# Generated by Django 3.1.2 on 2020-10-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='candidate', max_length=100)),
                ('sentiment_score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('keywords', models.CharField(default='unspecified', max_length=100)),
                ('date', models.CharField(default='2020/10/01 12:05:00', max_length=50)),
                ('pn', models.CharField(default='unspecified', max_length=2)),
            ],
        ),
    ]