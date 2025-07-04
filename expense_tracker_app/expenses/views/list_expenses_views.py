from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from serializers import ExpensesIncomeSeralizers
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def expense_list(request):
    return Response({"expenses": []})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_expenses_record(request):
    serializer = ExpensesIncomeSeralizers(data= request.data)
    # Adding record only when data is valid

    if serializer.is_valid():
        serializer.save(user = request.user) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)