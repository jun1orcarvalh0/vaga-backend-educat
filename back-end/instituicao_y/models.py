from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.cpf}'
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'
    

class Status(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'
    

class InstituicaoY(models.Model):
    nome = models.CharField(max_length=200)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ano_letivo = models.IntegerField()
    semetre = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    frequencia = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Instituição'

    def __str__(self):
        return f'{self.nome}'
