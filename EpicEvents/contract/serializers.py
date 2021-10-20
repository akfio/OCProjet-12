from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'client', 'status', 'amount', "payment_due", 'sales_contact')
