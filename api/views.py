from django.shortcuts import render

from .serializers import CustomerSerializer,WorkSerializer

from rest_framework.viewsets import ModelViewSet

from rest_framework import status,permissions,authentication

from rest_framework.response import Response

from rest_framework.decorators import action

from .models import Customer



class CustomerViewSetView(ModelViewSet):

    queryset=Customer.objects.all()

    serializer_class=CustomerSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(technician=self.request.user)
    
    @action(methods=['POST'],detail=True)
    def add_work(self,request,*args,**kwargs):

        # customer_data=self.get_object()

        id=kwargs.get('pk')

        customer_data=Customer.objects.get(id=id)

        serializer=WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_data)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.data)