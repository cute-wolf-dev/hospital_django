# Generated by Django 2.2.6 on 2019-10-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0008_auto_20191030_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='birthday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]