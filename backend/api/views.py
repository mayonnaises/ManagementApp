# api/views.py

from rest_framework.views import APIView

from .serializers import EmployeeDataSerializer


class EmployeeListAPI(APIView):
    '''Get employee list'''

    def get(self, request):
        pass
