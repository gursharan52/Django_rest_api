from django.contrib import admin
from django.urls import include, path
from crud.views import EmployeeListView, EmployeeDetailView, EmployeeDestroyView, EmployeeCreateView, EmployeeUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employees/create/', EmployeeCreateView.as_view(), name='EmployeeCreateView'),
    path('employees/<pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/<pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<pk>/delete/', EmployeeDestroyView.as_view(), name='employee-delete'),

]

