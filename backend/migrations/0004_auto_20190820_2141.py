# Generated by Django 2.1.4 on 2019-08-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_iteminfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='drop_rate',
            new_name='ChanceOrQuestChance',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='i_level',
            new_name='condition_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='entry',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='groupid',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='required_level',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='type',
            new_name='maxcount',
        ),
        migrations.AddField(
            model_name='item',
            name='mincountOrRef',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='patch_max',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='patch_min',
            field=models.TextField(blank=True),
        ),
    ]
