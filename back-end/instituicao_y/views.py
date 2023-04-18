from django.shortcuts import render
from rest_framework import viewsets

from .models import Aluno, Status, Disciplina, InstituicaoY
from .serializers import AlunoSerializer, StatusSerializer, DisciplinaSerializer, InstituicaoYSerializer


class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Escreva o necessário abaixo


class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class InstituicaoYView(viewsets.ModelViewSet):
    queryset = InstituicaoY.objects.all()
    serializer_class = InstituicaoYSerializer
