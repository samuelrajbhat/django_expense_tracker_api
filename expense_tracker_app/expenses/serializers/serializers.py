from rest_framework import serializers
from expense_tracker_app.expenses.models import ExpensesIncome

class ExpensesIncomeSeralizers( serializers.ModelSerializer):
    total = serializers.DecimalField(source = 'total', max_digits=12, decimal_places=2)
    class Meta:
        model = ExpensesIncome
        fields = [
            'is',
            'user',
            'title',
            'description',
            'amunt',
            'transaction_atype',
            'tax',
            'tax_type',
            'created_at',
            'updated_at',
            'total',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total']

        def create(self, validated_data):
            user = self.context['request'].user # type: ignore
            return ExpensesIncome.objects.create(user=user, **validated_data)