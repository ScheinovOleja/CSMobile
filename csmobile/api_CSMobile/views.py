from rest_framework.response import Response
from rest_framework.views import APIView
from CSMobile_site.models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


class AddData(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response({"employer": serializer.data})

    def post(self, request):
        employee = request.data.get('employer')
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": f"Article '{employee_saved}' created successfully"})