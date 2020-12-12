from rest_framework.response import Response
from rest_framework.views import APIView
from CSMobile_site.models import Employee, Contact, Status, CustomerContact, Contractor, Message
from .serializers import EmployeeSerializer, ContactSerializer, StatusSerializer, CustomerContactSerializer, \
    ContractorSerializer, MessageSerializer


# Create your views here.


class AddData(APIView):

    def __init__(self):
        super().__init__()
        self.employee = Employee.objects.all()
        self.contact = Contact.objects.all()
        self.status = Status.objects.all()
        self.customer = CustomerContact.objects.all()
        self.contractor = Contractor.objects.all()
        self.message = Message.objects.all()

    def get(self, request):
        employee_serializer = EmployeeSerializer(self.employee, many=True)
        contact_serializer = ContactSerializer(self.contact, many=True)
        status_serializer = StatusSerializer(self.status, many=True)
        customer_serializer = CustomerContactSerializer(self.customer, many=True)
        contractor_serializer = ContractorSerializer(self.contractor, many=True)
        message_serializer = MessageSerializer(self.message, many=True)

        return Response(
            {
                "employee": employee_serializer.data,
                "contact": contact_serializer.data,
                "status": status_serializer.data,
                "customer": customer_serializer.data,
                "contractor": contractor_serializer.data,
                "message": message_serializer.data,
            }
        )

    def post(self, request):
        employee = request.data.get('employee')
        contact = request.data.get('contact')
        status = request.data.get('status')
        customer = request.data.get('customer')
        contractor = request.data.get('contractor')
        message = request.data.get('message')
        employee_serializer = EmployeeSerializer(data=employee)
        contact_serializer = ContactSerializer(data=contact)
        status_serializer = StatusSerializer(data=status)
        customer_serializer = CustomerContactSerializer(data=customer)
        contractor_serializer = ContractorSerializer(data=contractor)
        message_serializer = MessageSerializer(data=message)
        if employee_serializer.is_valid(raise_exception=True):
            employee_serializer.save()
        if contact_serializer.is_valid(raise_exception=True):
            contact_serializer.save()
        if status_serializer.is_valid(raise_exception=True):
            status_serializer.save()
        if customer_serializer.is_valid(raise_exception=True):
            customer_serializer.save()
        if contractor_serializer.is_valid(raise_exception=True):
            contractor_serializer.save()
        if message_serializer.is_valid(raise_exception=True):
            message_serializer.save()
        return Response({"success": f"Created successfully"})
