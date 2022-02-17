from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializers import*
from rest_framework import status


'''QUERYSET OBJECTS SECTION'''
@api_view(['GET','POST'])
def api_customers(request):
    '''http://127.0.0.1:8000/api/customers'''

    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = Customer_Serializer(customers,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Customer_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def api_goods(request):

    if request.method == 'GET':
        goods = Good.objects.all()
        serializer = Good_Serializer(goods, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Good_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




'''DETAILISED OBJECT API'''

@api_view(['GET','PUT','PATCH','DELETE'])
def api_customer_detail(request, pk):
    '''http://127.0.0.1:8000/api/customer/<pk>/'''
    client = Customer.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = Customer_Serializer(client)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = Customer_Serializer(client,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','PATCH','DELETE'])
def api_goods_detail(request,pk):
    '''http://127.0.0.1:8000/api/good/<pk>/'''
    good = Good.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = Good_Serializer(good)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = Good_Serializer(good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Done!