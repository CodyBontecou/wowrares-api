# Generated by Django 2.1.4 on 2018-12-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='drop_rate',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='i_level',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='required_level',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]