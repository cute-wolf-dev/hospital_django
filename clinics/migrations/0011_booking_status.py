# Generated by Django 2.2.6 on 2019-11-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0010_booking_clinic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
