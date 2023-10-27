export interface Especialidade{
  idEspecialidade: number;
  descricaoEspecialidade: string;
  selecionada?: boolean;
}

export interface ProfissionalTrataEspecialidade{
  idEspecialidade: number;
  cpfProfissional: string;
}
