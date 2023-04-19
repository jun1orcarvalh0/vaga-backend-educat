from rest_framework import serializers

from .models import Aluno, Disciplina, Status, InstituicaoX


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

# escreva o que for necessário abaixo


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class InstituicaoXSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoX
        fields = '__all__'
