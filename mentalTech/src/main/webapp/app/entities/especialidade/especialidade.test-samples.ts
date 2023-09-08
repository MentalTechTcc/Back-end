import { IEspecialidade, NewEspecialidade } from './especialidade.model';

export const sampleWithRequiredData: IEspecialidade = {
  id: 27193,
  idEspecialidade: 4820,
};

export const sampleWithPartialData: IEspecialidade = {
  id: 4133,
  idEspecialidade: 9793,
};

export const sampleWithFullData: IEspecialidade = {
  id: 12710,
  idEspecialidade: 9128,
  nomeEspecialidade: 'Casa',
};

export const sampleWithNewData: NewEspecialidade = {
  idEspecialidade: 1162,
  id: null,
};

Object.freeze(sampleWithNewData);
Object.freeze(sampleWithRequiredData);
Object.freeze(sampleWithPartialData);
Object.freeze(sampleWithFullData);
