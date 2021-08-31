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

    def get(self, request):
        department_list = self.get_objects()
        serializer =  DepartmentDataSerializer(
            department_list, many=True)
        return Response(serializer.data)