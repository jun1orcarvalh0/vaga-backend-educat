from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100, null=True, blank=True)
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=20)
    

class Status(models.Model):
    nome = models.CharField(max_length=20)
    

class InstituicaoX(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ano_letivo = models.IntegerField()
    semetre = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    frequencia = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)