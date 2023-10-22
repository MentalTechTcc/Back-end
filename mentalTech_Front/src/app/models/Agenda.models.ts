import { Time } from "@angular/common";

export interface Agenda {
    data: Date;
    hora: Time;
    duracao: number;
    modalidadeAtendimento: string;
    cpfProfissional:String;
    ocupado:boolean;
  }
  