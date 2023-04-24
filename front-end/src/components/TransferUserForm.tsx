'use-client';

import { useForm } from 'react-hook-form';

import { zodResolver } from '@hookform/resolvers/zod';
import { validateStudent } from 'api/fetchApi';
import { z } from 'zod';

const schema = z.object({
  cpf: z.string().min(11, 'O CPF deve ter 11 dígitos.')
});

type FormProps = z.infer<typeof schema>;

export default function TransferUserForm() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<FormProps>({
    mode: 'all',
    reValidateMode: 'onChange',
    resolver: zodResolver(schema)
  });

  console.log(errors.cpf);

  const handleForm = (data: FormProps) => {
    const { cpf } = data;
    const result = validateStudent({ cpf });
    console.log(result);
  };

  return (
    <div className="flex w-full h-screen items-center justify-center">
      <div>
        <div className="flex bg-white px-10 py-10 rounded-3xl border-2 border-gray-200">
          <form onSubmit={handleSubmit(handleForm)}>
            <div className="flex flex-col p-4">
              <label className="text-xl font-medium mb-6">
                Digite o CPF do Aluno:
              </label>
              <input
                className="w-full border-2 border-gray-100 rounded-lg p-4 mt-1 bg-transparent"
                {...register('cpf')}
                type="text"
                placeholder="Insira o CPF"
                maxLength={11}
              />
              {errors.cpf?.message && (
                <p className="text-red-600">{errors.cpf.message}</p>
              )}
            </div>
            <div className="mt-8 flex flex-col">
              <button
                type="submit"
                className={
                  'py-3 rounded-xl bg-blue-600 text-white text-lg font-semibold hover:bg-green-700'
                }
              >
                Realizar transfêrencia
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
