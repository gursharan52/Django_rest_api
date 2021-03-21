from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDetailView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeUpdateView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()    

class EmployeeDestroyView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()    