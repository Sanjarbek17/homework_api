# Generated by Django 4.1.1 on 2022-11-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attempt',
            field=models.IntegerField(default=1),
        ),
    ]