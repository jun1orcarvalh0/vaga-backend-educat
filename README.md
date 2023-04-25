# Teste vaga backend

Olá candidato, nesse teste será esperado os seguintes critérios de aceitação:

* Não será necessario subir qualquer tipo de alteração para este repositório, o resultado do teste, pode ser enviado para um repositório do candidato ou enviado por email devolta ao avaliador.

* Codigo limpo seguindo a arquitetura do framework Django REST.

* Resultados sendo enviados para a tabela de destino de acordo com as regras propostas.

* Poderá ser feito utilizando o banco de dados SQLite do próprio framework ou outro caso o candidato desejar.

* O front-end deverá ser feito para interagir com o back-end mas não sera avaliado mas é um diferencial, não é necessário nenhum tipo de estilização e etc, apenas uma interface que consiga interagir com a API.


# Inicial:

* Tenha certeza de estar com python 3.7 a 3.8, e seus comandos podem variar de `python` a `python3` e `pip` a `pip3` 

* Para rodar o projeto, as dependências estão especificados no `requirements.txt`

* Para utiliza-los utilize `$ pip install -r requirements.txt`, as dependências serão instaladas.

# Para rodar o Front-End:

* Certifique-se de estar na pasta 'front-end'

* Para instalar as depêndencias utilize `$ npm install`

* Para rodar o projeto `$ npm run dev`

* O front-end rodará na porta 3000

* Tenha certeza que a porta 3000 não está alocada, pois o back-end espera que a requisição seja feita através dessa porta.


# Contexto:

- A instituição X precisa transferir um candidato proveniente da instituição Y.

- O candidato solicitou transferência para o segundo semestre do segundo ano letivo do curso.

Regras de TRANSFERÊNCIA:

- O candidato deve possuir vínculo ativo com a instituição de origem;

- As disciplinas da grade curricular da instituição Y que sejam equivalentes com a nova grade da instituição X, e cumpram os requisitos mínimos de Carga Horária e Frequência deverão ser dispensadas.

OBS: Dispensa de disciplina refere-se ao aproveitamento dos estudos realizados em outra instituição, ou seja, as disciplinas aprovadas na instituição de origem e que podem ser aproveitadas também estarão aprovadas na nova institução.

- As disciplinas da grade curricular da instituição Y que se encontrem atualmente cursando e sejam equivalentes com a nova grade da instituição X, deverão continuar sendo cursadas pelo candidato, caso cumprir o requisito mínimo de Carga Horária equivalente.

- As disciplinas da grade curricular da instituição Y que se encontrem atualmente reprovadas e sejam equivalentes com a nova grade da instituição X, deverão ser cursadas pelo candidato, caso cumprir o requisito mínimo de Carga Horária equivalente.

# Exemplos de URL:

http://localhost:8000/instituicao-y/alunos

http://localhost:8000/admin

# Considerações:
* Como não foi especificado como eu deveria fazer a validação do vínculo ativo, alterei os campos já implementados para que não fosse possível criar um novo usuário com cpf e/ou email já existentes na tabela de Alunos da Instituicao_X e Instituicao_Y.
* Com relação a transfêrencia de um aluno, alguns pontos não ficaram muito nítidos para mim com relação as regras de negócio. Mas seguindo a minha interpretação do problema, estabeleci como Carga Horária equivalente aquela que na instituicao_y fosse maior ou igual a Carga Horária exigida em instituicao_x. E a partir disso, todas as disciplinas já aprovadas que tivesse uma Carga Horária exigida em y menor que em x, deveriam mudar seu status para "a cursar".