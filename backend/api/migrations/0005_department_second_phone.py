# Generated by Django 3.2.6 on 2021-08-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_department_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='second_phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
