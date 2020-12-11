from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework import permissions
from crud.serializers import EmployeeSerializer
from crud.models import Employee



class get_delete_update_employee(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return employee

    # Get a employee
    def get(self, request, pk):
        sr_no = pk
        employee = self.get_queryset(sr_no)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a employee
    def put(self, request, pk):
        
        employee = self.get_queryset(pk)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a employee
    def delete(self, request, pk):

        employee = self.get_queryset(pk)

        employee.delete()
        content = {
            'status': 'NO CONTENT'
            }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
   

class get_post_employees(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
       employee = Employee.objects.all()
       return employee

    # Get all employees
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    # Create a new employees
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)