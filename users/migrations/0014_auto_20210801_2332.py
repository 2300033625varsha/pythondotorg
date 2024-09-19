# Generated by Django 3.2.5 on 2021-08-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180705_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='psf_announcements',
            field=models.BooleanField(blank=True, null=True, verbose_name='I would like to receive occasional PSF email announcements'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='psf_code_of_conduct',
            field=models.BooleanField(blank=True, null=True, verbose_name='I agree to the PSF Code of Conduct'),
        )
    ]