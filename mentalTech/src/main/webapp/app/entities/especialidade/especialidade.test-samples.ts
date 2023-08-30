import { IEspecialidade, NewEspecialidade } from './especialidade.model';

export const sampleWithRequiredData: IEspecialidade = {
  id: 13099,
  idEspecialidade: 30886,
};

export const sampleWithPartialData: IEspecialidade = {
  id: 20342,
  idEspecialidade: 30978,
  nomeEspecialidade: 'bronze Masculino Iêmen',
};

export const sampleWithFullData: IEspecialidade = {
  id: 13375,
  idEspecialidade: 24701,
  nomeEspecialidade: 'Feminino Desenvolvedor',
};

export const sampleWithNewData: NewEspecialidade = {
  idEspecialidade: 31454,
  id: null,
};

Object.freeze(sampleWithNewData);
Object.freeze(sampleWithRequiredData);
Object.freeze(sampleWithPartialData);
Object.freeze(sampleWithFullData);
