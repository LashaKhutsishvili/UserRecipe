from rest_framework.decorators import permission_classes

from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer