export interface Relatorio{
  descricao: string;
  idConsulta: number;
  dataCadastro: Date;
}

export interface RelatorioRequestId{
  idRelatorio: number;
  descricao: string;
  idConsulta: number;
  dataCadastro: Date;
}