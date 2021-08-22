# api/serializers.py

from rest_framework.serializers import ModelSerializer

from .models import Employee


class EmployeeDataSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'name_reading', 'phone_number', 'note']