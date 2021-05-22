from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer

from .models import Project


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/project-list/',
		'Detail View':'/project-detail/<str:pk>/',
		'Create':'/project-create/',
		'Update':'/project-update/<str:pk>/',
		'Delete':'/project-delete/<str:pk>/',
		}

	return Response(api_urls)


    # return JsonResponse("api base view", safe=False)           #  testing

@api_view(['GET'])
def projectList(request):
	project = Project.objects.all().order_by('-id')
	serializer = ProjectSerializer(project, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request, pk):
	project = Project.objects.get(id=pk)
	serializer = ProjectSerializer(project, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def projectCreate(request):
	serializer = ProjectSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
   
	return Response(serializer.data)

@api_view(['PUT'])
def projectUpdate(request, pk):
	project = Project.objects.get(id=pk)
	serializer = ProjectSerializer(instance=project, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def projectDelete(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()

	return Response('Item succsesfully delete!')