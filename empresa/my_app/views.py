from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Empregado, Departamento
from .serializers import EmpregadoSerializer, DepartamentoSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics

#@csrf_exempt
#@api_view(['GET', 'POST'])
#def empregado_list(request):

#    if request.method == 'GET':
#        empregados = Empregado.objects.all()
#        serializer = EmpregadoSerializer(empregados, many=True)
#        return JsonResponse(serializer.data, safe=False)

#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = EmpregadoSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data, status=201)
#        return JsonResponse(serializer.errors, status=400)

#@csrf_exempt
#@api_view(['GET', 'POST'])
#def departamento_list(request):
#    if request.method == 'GET':
#        departamentos = Departamento.objects.all()
#        serializer = DepartamentoSerializer(departamentos, many=True)
#        return JsonResponse(serializer.data, safe=False)

#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = DepartamentoSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data, status=201)
#        return JsonResponse(serializer.errors, status=400)

#@csrf_exempt
#@api_view(['GET', 'PUT', 'DELETE'])
#def empregado_detail(request, pk):
#    try:
#        empregado = Empregado.objects.get(pk=pk)
#    except Empregado.DoesNotExist:
#        return HttpResponse(status=404)

#    if request.method == 'GET':
#        serializer = EmpregadoSerializer(empregado)
#        return JsonResponse(serializer.data)

#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = EmpregadoSerializer(empregado, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#       return JsonResponse(serializer.errors, status=400)

#    elif request.method == 'DELETE':
#        empregado.delete()
#        return HttpResponse(status=204)

#@csrf_exempt
#@api_view(['GET', 'PUT', 'DELETE'])
#def departamento_detail(request, pk):
#    try:
#       departamento = Departamento.objects.get(pk=pk)
#    except Departamento.DoesNotExist:
#        return HttpResponse(status=404)

#    if request.method == 'GET':
#        serializer = DepartamentoSerializer(departamento)
#        return JsonResponse(serializer.data)

#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = DepartamentoSerializer(departamento, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#        return JsonResponse(serializer.errors, status=400)

#    elif request.method == 'DELETE':
#        departamento.delete()
#        return HttpResponse(status=204)

class EmpregadoList(APIView):
    def get(self, request, format=None):
        empregados = Empregado.objects.all()
        serializer = EmpregadoSerializer(empregados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpregadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentoList(APIView):
    def get(self, request, format=None):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpregadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empregado.objects.get(pk=pk)
        except Empregado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empregado = self.get_object(pk)
        serializer = EmpregadoSerializer(empregado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empregado = self.get_object(pk)
        serializer = EmpregadoSerializer(empregado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        empregado = self.get_object(pk)
        empregado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        departamento = self.get_object(pk)
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Empregado.objects.all()
#     serializer_class = EmpregadoSerializer
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Departamento.objects.all()
#     serializer_class = DepartamentoSerializer
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Empregado.objects.all()
#     serializer_class = EmpregadoSerializer
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Departamento.objects.all()
#     serializer_class = DepartamentoSerializer