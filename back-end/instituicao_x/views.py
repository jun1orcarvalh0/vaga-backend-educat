# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from instituicao_y.models import InstituicaoY, Aluno as AlunoY
from instituicao_y.serializers import AlunoSerializer as AlunoYSerializer, InstituicaoYSerializer
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

        new_student_serializer = AlunoSerializer(data=request.data)

        if new_student_serializer.is_valid():
            new_student_serializer.save()

            student_instituicao_y = AlunoYSerializer(
                AlunoY.objects.get(cpf=request.data["cpf"]))

            student_instituicao_x = AlunoSerializer(
                Aluno.objects.get(cpf=request.data["cpf"]))

            instituicao_y = InstituicaoYSerializer(
                InstituicaoY.objects.filter(
                    aluno_id=student_instituicao_y.data["id"]), many=True)

            # student_subjects_transfer = []

            for disciplina_y in instituicao_y.data:

                disciplina_y_dict = dict(disciplina_y)

                find_disciplina_in_instituicao_x = DisciplinaSerializer(
                        Disciplina.objects.get(id=disciplina_y_dict["id"]))

                if (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 1):

                    exigencias = {"carga_horaria": 20,"frequencia_minima": 18}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"] and disciplina_y_dict["frequencia"] >= exigencias["frequencia_minima"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=1
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)
                    else:
                        print('disciplina1 a cursar')

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 2):

                    exigencias = {"carga_horaria": 16,"frequencia_minima": 11}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"] and disciplina_y_dict["frequencia"] >= exigencias["frequencia_minima"]):
                        print('aprovado')
                    else:
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=1
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 3):

                    exigencias = {"carga_horaria": 11, "frequencia_minima": 11}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=4
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 4):

                    exigencias = {"carga_horaria": 15, "frequencia_minima": 10}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=4
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 5):

                    exigencias = {"carga_horaria": 16, "frequencia_minima": 11}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=4
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 6):

                    exigencias = {"carga_horaria": 18,"frequencia_minima": 18}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"] and disciplina_y_dict["frequencia"] >= exigencias["frequencia_minima"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=1
                        )
                        student_subject_transfer.save()
                    else:
                        print('disciplina6 a cursar')
             
                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 7):

                    exigencias = {"carga_horaria": 17, "frequencia_minima": 16}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"]):
                        print('disciplina7 cursando')
                    else:
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=4
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)

                elif (find_disciplina_in_instituicao_x and disciplina_y_dict["id"] == 8):

                    exigencias = {"carga_horaria": 8, "frequencia_minima": 5}

                    if (disciplina_y_dict["carga_horaria"] >= exigencias["carga_horaria"]):
                        student_subject_transfer = InstituicaoX(
                                nome="Instituicao X",
                                ano_letivo=disciplina_y_dict["ano_letivo"],
                                semestre=disciplina_y_dict["semestre"],
                                carga_horaria=exigencias["carga_horaria"],
                                frequencia_minima=exigencias["frequencia_minima"],
                                aluno_id=student_instituicao_x.data["id"],
                                disciplina_id=disciplina_y_dict["id"],
                                status_id=3
                        )
                        student_subject_transfer.save()
                        # student_subjects_transfer.append(result)
                    else:
                        print('disciplina8 a cursar')

            return Response('Transferência realizada com sucesso',
                            status=status.HTTP_201_CREATED)

        return Response(
            new_student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class InstituicaoXView(viewsets.ModelViewSet):
    queryset = InstituicaoX.objects.all()
    serializer_class = InstituicaoXSerializer
