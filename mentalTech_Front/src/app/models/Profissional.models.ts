export interface Profissional{
  nome: string;
  senha: string;
  dataNascimento: Date;
  telefone: string;
  email: string;
  administrador: boolean;
  sexo: number;
  codigoProfissional: string;
  descricaoProfissional: string;
  cpf: string;
  pix: string;
}

export interface ProfissionalRequestId{
  idPessoa:string;
  nome: string;
  senha: string;
  dataNascimento: Date;
  telefone: string;
  email: string;
  administrador: boolean;
  sexo: number;
  codigoProfissional: string;
  descricaoProfissional: string;
  cpf: string;
  linkPagamento: string;
}
