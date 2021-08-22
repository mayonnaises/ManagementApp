# Generated by Django 3.2.6 on 2021-08-22 03:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('name_reading', models.CharField(max_length=50, verbose_name='name reading')),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,14}$')], verbose_name='mobile number')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '従業員',
                'ordering': ['-created_at'],
            },
        ),
    ]
