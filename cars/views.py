from .models import Car
from .serializers import CarSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def car_list(request, format = None):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many = True)  
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        print("WE ARE HERE")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            print("serialzier did not save")
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        

@api_view(['GET','PUT','DELETE'])
def car_detail(request, id, format = None):
    try:
       car = Car.objects.get(pk = id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #get the car info by ID
    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    #edit car info by ID
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)
    
    #delete car info by ID
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


        
    