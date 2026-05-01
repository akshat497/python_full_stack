from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
# Create your views here.
from .models import Todo
from .serializer import TodoSerializer


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])

def todo_create(request):
    print(request.data)
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "created successfully", "data": serializer.data})
    return Response(serializer.errors, status=400,)


@api_view(['DELETE'])
def todo_delete(request, id):
    Todo.objects.filter(id=id).delete()
    return Response({"message": "deleted successfully"})
            
        
        