from django.contrib import admin


from .models import Aluno, Status, Disciplina, InstituicaoY

@admin.register(InstituicaoY)
class InstituicaoYAdmin(admin.ModelAdmin):
    pass


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass
