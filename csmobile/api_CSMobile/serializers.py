from rest_framework import serializers

from CSMobile_site.models import Employee, Contact, Status, CustomerContact, Contractor, Message


class EmployeeSerializer(serializers.Serializer):
    guid = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class ContactSerializer(serializers.Serializer):
    guid = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)


class StatusSerializer(serializers.Serializer):
    state = serializers.CharField()

    def create(self, validated_data):
        return Status.objects.create(**validated_data)


class CustomerContactSerializer(serializers.Serializer):
    employee = serializers.IntegerField()
    client = serializers.IntegerField()
    appeal = serializers.CharField()

    def create(self, validated_data):
        return CustomerContact.objects.create(**validated_data)


class ContractorSerializer(serializers.Serializer):
    guid = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    inn = serializers.CharField()

    def create(self, validated_data):
        return Contractor.objects.create(**validated_data)


class MessageSerializer(serializers.Serializer):
    guid = serializers.CharField()
    date = serializers.DateTimeField()
    number = serializers.CharField()
    customer = serializers.IntegerField()
    contact = serializers.IntegerField()
    status = serializers.IntegerField()
    customer_contacts = serializers.IntegerField()
    executor = serializers.IntegerField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
