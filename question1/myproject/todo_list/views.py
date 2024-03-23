from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import serializers
from . import models
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TodoListApiView(APIView):

    def get_object(self, item_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return models.Item.objects.get(id=item_id)
        except models.Item.DoesNotExist:
            return None
    
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo item with given todo data
        '''
        # data = {
        #     'title': request.data.get('title'), 
        #     'detail': request.data.get('detail'),
        #     'is_completed': request.data.get('is_completed'),
        # }
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, item_id, *args, **kwargs):
        '''
        Updates the todo item with given item_id if exists
        '''
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'detail': request.data.get('detail'),
            'is_completed': request.data.get('is_completed'), 
        }
        serializer = serializers.ItemSerializer(instance = item_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, item_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(item_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")