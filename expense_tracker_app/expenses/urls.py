from django.urls import path
from .views import expenses, expense_detail


urlpatterns = [
    path('expenses/',expenses, name='expenses'),
    path('expenses/<int:id>', expense_detail, name='expense-id')
]