export interface Paciente{
  nome: string;
  senha: string;
  dataNascimento: Date;
  telefone: string;
  email: string;
  administrador: boolean;
  sexo: number;
}

export interface PacienteResponse{
  idPessoa: number;
  nome: string;
  senha: string;
  dataNascimento: Date;
  telefone: string;
  email: string;
  administrador: boolean | null;
  sexo: boolean | null;
}
