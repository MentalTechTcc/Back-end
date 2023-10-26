export interface Tematica{
  nomeTematica: string;
}

export interface TematicaResponse{
  nomeTematica: string;
  idTematicasPrincipais: number;
}


export interface ProfissionalTrataTematica{
  idTematicasPrincipais: number;
  cpfProfissional: string;
}

