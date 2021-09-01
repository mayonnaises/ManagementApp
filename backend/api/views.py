# api/views.py

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Department, Employee
from .serializers import (
    DepartmentDataSerializer,
    EmployeeDataSerializer
)


class EmployeeListAPI(APIView):
    '''Get employee list'''

    def get_objects(self):
        try:
            return Employee.objects.all()
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request):
        employee_list = self.get_objects()
        serializer = EmployeeDataSerializer(employee_list, many=True)
        return Response(serializer.data)


class DepartmentListAPI(APIView):

    def get_objects(self):
        try:
            return Department.objects.all()
        except Department.DoesNotExist:
            raise Http404

    def get_employee_data(self, serializer):
        for data in serializer.data:
            employee = Employee.objects.get(pk=data['employee'])
            data['employee_name'] = employee.name
            data['employee_phone'] = employee.phone_number

    def get(self, request):
        department_list = self.get_objects()
        serializer =  DepartmentDataSerializer(
            department_list, many=True)

        self.get_employee_data(serializer)

        return Response(serializer.data)


class DepartmentDetailAPI(APIView):

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        department = self.get_object(pk)
        serializer = DepartmentDataSerializer(department)
        data = serializer.data
        employee = Employee.objects.get(pk=data['employee'])
        data.update({
            'employee_name': employee.name,
            'employee_phone': employee.phone_number
        })
        return Response(data)