from rest_framework import serializers
from crud.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','sr_no', 'first_name', 'last_name', 'email']

