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
    contractor = ContractorSerializer()
    customer_contacts = CustomerContactSerializer()
    executor = EmployeeSerializer()
    status = StatusSerializer()

    class Meta:
        model = Message
        fields = (
            'guid', 'date', 'number', 'contact', 'contractor', 'customer_contacts', 'executor', 'status')

    def create(self, validated_data):
        contact = Contact.objects.update_or_create(**validated_data.pop('contact'))[0].id

        executor = Employee.objects.update_or_create(**validated_data.pop('executor'))[0].id

        customer_contacts = CustomerContact.objects.update_or_create(
            appeal=validated_data.pop('customer_contacts')['appeal'],
            employee_id=executor,
            client_id=contact
        )[0].id

        contractor = Contractor.objects.update_or_create(**validated_data.pop('contractor'))[0].id

        status = Status.objects.update_or_create(**validated_data.pop('status'))[0].id

        message = Message.objects.update_or_create(
            guid=validated_data['guid'],
            date=validated_data['date'],
            number=validated_data['number'],
            contact_id=contact,
            contractor_id=contractor,
            customer_contacts_id=customer_contacts,
            executor_id=executor,
            status_id=status
        )

        return message[0]
