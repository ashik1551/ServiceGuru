from django.shortcuts import render

from .serializers import CustomerSerializer

from rest_framework.viewsets import ModelViewSet

from rest_framework import status,permissions,authentication

from rest_framework.response import Response

from .models import Customer



class CustomerViewSetView(ModelViewSet):

    queryset=Customer.objects.all()

    serializer_class=CustomerSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(technician=self.request.user)