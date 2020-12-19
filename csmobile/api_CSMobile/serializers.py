from rest_framework import serializers

from CSMobile_site.models import Employee, Contact, Status, CustomerContact, Contractor, Message


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('guid', 'code', 'name', 'phone', 'email')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('guid', 'code', 'name', 'phone', 'email')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('state',)


class CustomerContactSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    client = ContactSerializer()

    class Meta:
        model = CustomerContact
        fields = ('employee', 'client', 'appeal')


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('guid', 'code', 'name', 'inn')


class MessageSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    customer = ContractorSerializer()
    customer_contacts = CustomerContactSerializer()
    executor = EmployeeSerializer()
    status = StatusSerializer()

    class Meta:
        model = Message
        fields = (
            'guid', 'date', 'number', 'contact', 'customer', 'customer_contacts', 'executor', 'status')

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        customer_data = validated_data.pop('customer')
        customer = Contractor.objects.create(**customer_data)
        executor_data = validated_data.pop('executor')
        executor = Employee.objects.create(**executor_data)
        status_data = validated_data.pop('status')
        status = Status.objects.create(**status_data)
        customer_contact_data = validated_data.pop('customer_contacts')
        customer_contact = CustomerContact.objects.create(
            appeal=customer_contact_data['appeal'],
            employee_id=executor.id,
            client_id=contact.id
        )

        message = Message.objects.create(
            guid=validated_data['guid'],
            date=validated_data['date'],
            number=validated_data['number'],
            contact_id=contact.id,
            customer_id=customer.id,
            customer_contacts_id=customer_contact.id,
            executor_id=executor.id,
            status_id=status.id,
        )

        return message
