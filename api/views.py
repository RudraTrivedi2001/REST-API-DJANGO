from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework import status
from .serializer import UserSerializer

@api_view(['GET'])   #get users
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['POST'])     #to add a user 
def create_User(request):
    serializer = UserSerializer(data = request.data) # we are serializing the data that is coming fronm the front end
    if serializer.is_valid():  #if data is valid we are saving it to the db 
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_200_OK)   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    try: 
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    


    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            user.delete()
            return Response({"message" : "User Deleted successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message" : "There is no such user to delete"}, status=status.HTTP_400_BAD_REQUEST)

        
       


    