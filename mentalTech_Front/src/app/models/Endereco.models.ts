export interface Endereco {
  cep: string;
  estado: string;
  cidade: string;
  bairro: string;
  numero: number;
  complemento: string;
}

export interface EnderecoResponse {
  idEndereco: number;
  cep: string;
  estado: string;
  cidade: string;
  bairro: string;
  numero: number;
  complemento: string;
}
