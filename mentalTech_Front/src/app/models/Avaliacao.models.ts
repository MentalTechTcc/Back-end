import { Time } from "@angular/common";

export interface Avaliacao {
    cpfProfissional: string ;
    idPessoa: number ;
    notaGeral: number ;
    notaPontualidade: number ;
    notaAtendimento: number ;
    observacoes: string ;
    dataCadastro :  Date;
  }
  

  export interface AvaliacaoRequestId {
    idAvaliacao:number;
    cpfProfissional: string ;
    idPessoa: number ;
    notaGeral: number ;
    notaPontualidade: number ;
    notaAtendimento: number ;
    observacoes: string ;
    dataCadastro :  Date;
    observacoesExpandidas: boolean;
  }
