import { Time } from "@angular/common";

export interface Agenda {
    data: Date;
    hora: Time;
    duracao: number;
    modalidadeAtendimento: number;
    cpfProfissional:String;
    ocupado:boolean;
    valorProposto:number;
    linkPagamento: string;
    idEndereco?:number;
  }


export interface AgendaRequestId {
  idAgenda:number;
  data: Date;
  hora: Time;
  duracao: number;
  modalidadeAtendimento: number;
  cpfProfissional:String;
  ocupado:boolean;
  valorProposto:number;
  linkPagamento: string;
  idEndereco?:number;

}
