# Generated by Django 3.2.6 on 2021-08-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210831_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='phone number'),
        ),
    ]
