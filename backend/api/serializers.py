# api/serializers.py

from rest_framework.serializers import ModelSerializer

from .models import Department, Employee


class EmployeeDataSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'name_reading',
            'phone_number',
            'note'
        ]


class DepartmentDataSerializer(ModelSerializer):

    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'name_reading',
            'employee',
            'address',
            'phone_number',
            'note'
        ]