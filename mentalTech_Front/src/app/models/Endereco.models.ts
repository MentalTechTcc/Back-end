export interface Endereco {
  cep: string;
  estado: string;
  cidade: string;
  bairro: string;
  numero: number;
  complemento: string;
}

export interface EnderecoResponse {
  cep: string;
  estado: string;
  cidade: string;
  bairro: string;
  numero: number;
  complemento: string;
  idEndereco: number;
}

export interface ProfissionalTemEndereco{
  idEndereco: number;
  cpfProfissional: string;
  detalhes?: EnderecoResponse; 
}
