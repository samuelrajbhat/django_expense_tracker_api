
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..models import ExpensesIncome
from ..serializers.serializers import ExpensesIncomeSeralizers
from rest_framework.decorators import api_view, permission_classes


from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def expenses(request):
    user = request.user
    if request.method == 'GET':
        # Implementing super_user features
        if user.is_superuser:
            queryset = ExpensesIncome.objects.all().order_by('-created_at')
        else:
            queryset = ExpensesIncome.objects.filter(user=user).order_by('-created_at')
        paginator = PageNumberPagination()
        # Declaree page size
        paginator.page_size = 25
        page = paginator.paginate_queryset(queryset, request)  # Set paginator.page here
        serializer = ExpensesIncomeSeralizers(page, many=True)
        return paginator.get_paginated_response(serializer.data)  # Now paginator.page exists

    elif request.method == 'POST':
        serializer = ExpensesIncomeSeralizers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def expense_detail(request, id):
    """
    Handles:
    - GET /api/expenses/{id}/ → Get specific record
    - PUT /api/expenses/{id}/ → Update specific record
    - DELETE /api/expenses/{id}/ → Delete specific record
    """
    try:
        expense = ExpensesIncome.objects.get(id=id, user=request.user)
    except ExpensesIncome.DoesNotExist:
        return Response({"error": "Record not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpensesIncomeSeralizers(expense)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ExpensesIncomeSeralizers(expense, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        expense.delete()
        return Response({"message": "Record deleted."}, status=status.HTTP_204_NO_CONTENT)
