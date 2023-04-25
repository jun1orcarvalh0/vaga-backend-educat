from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import AlunoView, DisciplinaView, StatusView, InstituicaoYView


router = routers.SimpleRouter(trailing_slash=False)
router.register('alunos', AlunoView, basename='personal-data')
# escreva o que for necessário abaixo
router.register('disciplina', DisciplinaView, basename='personal-data')
router.register('status', StatusView, basename='personal-data')
router.register('instituicao', InstituicaoYView, basename='personal-data')

urlpatterns = [] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
