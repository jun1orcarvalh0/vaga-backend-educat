'use-client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';

import { zodResolver } from '@hookform/resolvers/zod';
import { validateStudent } from 'api/fetchApi';
import { z } from 'zod';

type Student = {
  id: number;
  nome: string;
  email: string;
  cpf: string;
};

const schema = z.object({
  cpf: z.string().min(11, 'O CPF deve ter 11 dígitos.')
});

type FormProps = z.infer<typeof schema>;

export default function TransferUserForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isValid }
  } = useForm<FormProps>({
    mode: 'all',
    reValidateMode: 'onChange',
    resolver: zodResolver(schema)
  });

  const [student, setStudent] = useState({} as Student);

  const [errorMessage, setErrorMessage] = useState({
    isError: false,
    message: ''
  });

  console.log(errors.cpf);

  const handleValidateStudent = async (data: FormProps) => {
    const { cpf } = data;
    const result = await validateStudent({ cpf });
    if (result.message) {
      setStudent({ id: 0, nome: '', email: '', cpf: '' });
      return setErrorMessage({
        isError: true,
        message: 'Estudante não possui vínculo ativo!'
      });
    }
    setErrorMessage({ isError: false, message: '' });
    setStudent(result[0]);
  };

  const handleTransferStudent = () => {
    console.log(student);
  };

  return (
    <div className="flex w-full h-screen items-center justify-center">
      <div>
        <div className="flex flex-col bg-white p-20 rounded-3xl border-2 border-gray-200">
          <form
            onSubmit={handleSubmit(handleValidateStudent)}
            className="h-full w-full"
          >
            <div className="flex flex-col max-h-fit p-6">
              <label className="text-xl font-medium mb-4 text-center">
                Digite o CPF do Aluno:
              </label>
              <input
                className="w-full border-2 border-gray-100 rounded-lg p-4 mt-2 bg-transparent"
                {...register('cpf')}
                type="text"
                placeholder="Insira o CPF"
                maxLength={11}
              />
              {errors.cpf?.message && (
                <p className="text-red-600 mt-2">{errors.cpf.message}</p>
              )}
              <button
                type="submit"
                className={
                  !isValid
                    ? 'py-2 mt-5 rounded-xl bg-gray-600 text-white text-lg font-semibold'
                    : 'py-2 mt-5 rounded-xl bg-blue-600 text-white text-lg font-semibold hover:bg-blue-700'
                }
                disabled={!isValid}
              >
                Verificar Aluno
              </button>
              {errorMessage.isError && (
                <span className="text-red-600 mt-3 w-full">
                  {errorMessage.message}
                </span>
              )}
              {student.cpf && (
                <p className="text-gray-600 mt-3">
                  Estudante recuperado com sucesso!
                </p>
              )}
            </div>
          </form>
          <div className="flex flex-col mt-10">
            <button
              type="submit"
              className={
                student.cpf
                  ? 'py-2 mt-5 rounded-xl bg-blue-600 text-white text-lg font-semibold hover:bg-blue-700'
                  : 'py-2 mt-5 rounded-xl bg-gray-600 text-white text-lg font-semibold'
              }
              disabled={!student.cpf}
              onClick={() => handleTransferStudent()}
            >
              Realizar transfêrencia
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
