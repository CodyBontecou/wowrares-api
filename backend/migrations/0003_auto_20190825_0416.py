# Generated by Django 2.1.4 on 2019-08-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190820_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mob',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
