import dayjs from 'dayjs/esm';
import { sexoEnum } from 'app/entities/enumerations/sexo-enum.model';

export interface IPessoa {
  id: number;
  idPessoa?: number | null;
  nome?: string | null;
  dataNascimento?: dayjs.Dayjs | null;
  email?: string | null;
  sexo?: keyof typeof sexoEnum | null;
  telefone?: number | null;
  senha?: string | null;
}

export type NewPessoa = Omit<IPessoa, 'id'> & { id: null };
