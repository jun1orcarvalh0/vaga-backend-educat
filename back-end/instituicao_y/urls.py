from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import AlunoView



router = routers.SimpleRouter(trailing_slash=False)
router.register('alunos', AlunoView, basename='personal-data')
# escreva o que for necessário abaixo

urlpatterns = [] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)