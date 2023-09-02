from rest_framework import serializers
from .models import Empregado, Departamento

class EmpregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empregado
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'