from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from instituicao_y.models import Aluno as Aluno_instituicao_y
from .models import Aluno, Status, Disciplina, InstituicaoX
from .serializers import AlunoSerializer, StatusSerializer, DisciplinaSerializer, InstituicaoXSerializer


class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Escreva o necessário abaixo

    @action(detail=False, methods=['get'])
    def recuperar_aluno(self, request, pk=None):
        cpf = request.query_params.get('cpf')
        if not cpf:
            return Response(
                {"details": "O campo CPF não foi enviado"},
                status=status.HTTP_400_BAD_REQUEST)

        find_user = Aluno.objects.filter(cpf=cpf)

        if not find_user:
            return Response(
                {"details": "O Estudante não foi encontrado"},
                status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.get_serializer(find_user, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def transferencia_aluno(self, request, pk=None):
        find_user = Aluno_instituicao_y.objects.filter(cpf=request.data['cpf'])
        serializer = self.get_serializer(find_user, many=True)
        print(serializer.data)
        return Response(request.data)


class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class InstituicaoXView(viewsets.ModelViewSet):
    queryset = InstituicaoX.objects.all()
    serializer_class = InstituicaoXSerializer
