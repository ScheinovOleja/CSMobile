from rest_framework import serializers

from CSMobile_site.models import Employee


class EmployeeSerializer(serializers.Serializer):
    guid = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)