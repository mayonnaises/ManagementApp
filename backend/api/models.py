# api/models.py

import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        _('name'),
        max_length=20
    )
    name_reading = models.CharField(
        _('name reading'),
        max_length=50
    )
    phone_number = models.CharField(
        _('mobile number'),
        max_length=14,
        blank=True,
        null=True
    )
    note = models.TextField(
        _('note'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = '従業員'

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        _('name'),
        max_length=20
    )
    name_reading = models.CharField(
        _('name reading'),
        max_length=50,
        blank=True,
        null=True
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='department_employee',
        blank=True
    )
    postal_code = models.CharField(
        _('postal_code'),
        max_length=10,
        blank=True,
        null=True
    )
    address = models.CharField(
        _('address'),
        max_length=200,
        blank=True,
        null=True
    )
    number_of = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=14,
        blank=True,
        null=True
    )
    second_phone = models.CharField(
        max_length=14,
        blank=True,
        null=True
    )
    note = models.TextField(
        _('note'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = '部署'

    def __str__(self):
        return self.name