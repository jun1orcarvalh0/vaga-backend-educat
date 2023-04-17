from rest_framework import serializers

from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Aluno
		fields = ['id', 'nome', 'cpf']
        
# escreva o que for necessário abaixo