export interface IEspecialidade {
  id: number;
  idEspecialidade?: number | null;
  nomeEspecialidade?: string | null;
}

export type NewEspecialidade = Omit<IEspecialidade, 'id'> & { id: null };
