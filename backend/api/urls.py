# api/urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DepartmentListAPI, EmployeeListAPI


app_name = 'api'

urlpatterns = format_suffix_patterns([
    path('department_list/', DepartmentListAPI.as_view()),
    path('employee_list/', EmployeeListAPI.as_view()),
])