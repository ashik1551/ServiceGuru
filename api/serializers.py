from rest_framework import serializers

from .models import Customer,Work

class CustomerSerializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Customer

        fields="__all__"

        read_only_fields=['id','technician','status','created_date','update_date','is_active']