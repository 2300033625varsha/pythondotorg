# Generated by Django 2.2.24 on 2022-01-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0071_auto_20220113_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='requiredtextasset',
            name='max_length',
            field=models.IntegerField(blank=True, default=None, help_text='Limit to length of the input, empty means unlimited', null=True),
        ),
        migrations.AddField(
            model_name='requiredtextassetconfiguration',
            name='max_length',
            field=models.IntegerField(blank=True, default=None, help_text='Limit to length of the input, empty means unlimited', null=True),
        ),
    ]