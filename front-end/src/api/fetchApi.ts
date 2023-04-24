import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

export const validateStudent = async ({ cpf }: { cpf: string }) => {
  try {
    const result = await api.get('/instituicao-y/alunos/recuperar_aluno', {
      params: { cpf }
    });
    console.log(result);
    return result.data;
  } catch (error: any) {
    return error.toJSON();
  }
};
