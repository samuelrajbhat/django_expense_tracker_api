from rest_framework import serializers
from expenses.models import ExpensesIncome

class ExpensesIncomeSeralizers( serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    user = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = ExpensesIncome
        fields = [
            'id',
            'user',
            'title',
            'description',
            'amount',
            'transaction_type',
            'tax',
            'tax_type',
            'created_at',
            'updated_at',
            'total',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total']

    # def create(self, validated_data):
    #     user = self.context['request'].user # type: ignore
    #     return ExpensesIncome.objects.create(user=user, **validated_data)
    
   