export interface Consulta {
    valor:number;
    idAgenda: number;
    idPessoa:number;
    permiteCompartilharConhecimento:boolean;
    ocorreu:boolean;
  }
  

export interface ConsultaRequestId {
  idConsulta:number;
  valor:number;
  idAgenda: number;
  idPessoa:number;
  permiteCompartilhamento:boolean;
  ocorreu:boolean;
}