import dayjs from 'dayjs/esm';

import { sexoEnum } from 'app/entities/enumerations/sexo-enum.model';

import { IPessoa, NewPessoa } from './pessoa.model';

export const sampleWithRequiredData: IPessoa = {
  id: 19502,
  idPessoa: 8061,
  dataNascimento: dayjs('2023-09-08'),
  email: 'Clara.Macedo99@gmail.com',
  sexo: 'F',
};

export const sampleWithPartialData: IPessoa = {
  id: 15338,
  idPessoa: 4452,
  dataNascimento: dayjs('2023-09-07'),
  email: 'Arthur62@live.com',
  sexo: 'F',
  telefone: 11,
};

export const sampleWithFullData: IPessoa = {
  id: 20796,
  idPessoa: 10080,
  nome: 'Fantástico contas Alameda',
  dataNascimento: dayjs('2023-09-08'),
  email: 'JulioCesar_Melo98@yahoo.com',
  sexo: 'F',
  telefone: 11,
  senha: 'Rústico Produto',
};

export const sampleWithNewData: NewPessoa = {
  idPessoa: 19721,
  dataNascimento: dayjs('2023-09-08'),
  email: 'Caua_Barros90@yahoo.com',
  sexo: 'M',
  id: null,
};

Object.freeze(sampleWithNewData);
Object.freeze(sampleWithRequiredData);
Object.freeze(sampleWithPartialData);
Object.freeze(sampleWithFullData);
