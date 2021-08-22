# api/urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EmployeeListAPI


app_name = 'api'

urlpatterns = [
    path('employee_list/', EmployeeListAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)