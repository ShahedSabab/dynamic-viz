from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import wheatCanada
from .serializers import wheatCanadaSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def wheatCanada_list(request):
    if request.method == 'GET':
        data_list = wheatCanada.objects.all()
        serializer = wheatCanadaSerializers(data_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = wheatCanadaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def wheatCanada_detail(request, pk):
    try:
        wheat = wheatCanada.objects.get(pk=pk)
    except wheatCanada.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = wheatCanadaSerializers(wheat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = wheatCanadaSerializers(wheat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        wheat.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def wheatCanada_modify(request, token):

    param = 'null'
    for inp in token.split('&'):
        temp = inp.split('=')
        if(temp[0]=='year'):
            year = temp[1]
        elif (temp[0] == 'ah'):
            param = temp[0]
            value = temp[1]
        elif (temp[0] == 'dc'):
            param = temp[0]
            value = temp[1]
        elif (temp[0] == 'fdc'):
            param = temp[0]
            value = temp[1]
        elif (temp[0] == 'fc'):
            param = temp[0]
            value = temp[1]

    try:
        wheat = wheatCanada.objects.get(pk=year)
    except wheatCanada.DoesNotExist:
        return HttpResponse(status=404)
    request.method = 'PUT'
    temp = wheatCanadaSerializers(wheat)
    data = temp.data

    # check if any parameter has been passed
    if param != 'null':
        data[param] = value

    serializer = wheatCanadaSerializers(wheat, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)

# uncomment when not using any decorator for the API view
# @csrf_exempt
# # Create your views here.
# def wheatCanada_list(request):
#     if request.method == 'GET':
#         list = wheatCanada.objects.all()
#         serializer = wheatCanadaSerializers(list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = wheatCanadaSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def wheatCanada_detail(request, pk):
#     try:
#         wheat = wheatCanada.objects.get(pk=pk)
#     except wheatCanada.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = wheatCanadaSerializers(wheat)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         data['ah']=10000
#         serializer = wheatCanadaSerializers(wheat, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         wheat.delete()
#         return HttpResponse(status=204)

