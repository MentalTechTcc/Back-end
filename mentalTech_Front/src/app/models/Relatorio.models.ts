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
export interface RelatorioSave{
  descricao: string;
  idConsulta: number;
  dataCadastro: string;
}