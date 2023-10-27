export interface Tematica{
  nomeTematica: string;
}

export interface TematicaResponse{
  nomeTematica: string;
  idTematicasPrincipais: number;
  selecionada?: boolean;
}


export interface ProfissionalTrataTematica{
  idTematicasPrincipais: number;
  cpfProfissional: string;
}

