from django.shortcuts import render
from rest_framework import viewsets

from .models import Aluno
from .serializers import AlunoSerializer

class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
# Escreva o necessário abaixo
