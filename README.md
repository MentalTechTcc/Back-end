# Mental Tech

## Tecnologias do Projeto

<div style="display: flex">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original-wordmark.svg" width="50px"/>
    
<img src="https://icons8.com.br/icon/71257/angularjs" width="50px"/>
    
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="50px" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" width="50px"/>
</div>


## Como subir o ambiente do Back-end

- Primeiramente crie e/ou copie o arquivo `.env` e preencha com as configurações de acordo com o seu ambiente.
```
DB_CONNECT_URL=
SECRET_KEY=
JWT_ALGORITHM=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_HOURS=
ENV=DEV
```
- É necessário possuir o `docker ` e o `docker-compose` instalados na máquina
- Por fim execute o seguinte comando.

```bash
sudo docker-compose up --build
```
- As tabelas do banco de dados são geradas automaticamente.

## Como executar os testes

Caso esteja já esteja no `docker` basta executar o seguinte comando : 

```bash
PYTHONPATH=src TEST=true pytest -v -s
```

Caso contrário recomenda-se utilizar um [ambiente virtual](https://docs.python.org/3/tutorial/venv.html) para instalar as dependências e executar os testes, estando na raiz do projeto basta seguir os passos a seguir.

```bash
# Cria um ambiente virtual e utiliza ele como source
python3 -m venv venv
source venv/bin/activate

# Instalação das dependências
pip3 install -r requirements.txt

# Execução dos testes.
PYTHONPATH=src TEST=true pytest -v -s
```
## Como subir o ambiente do Front-end
Baixe o angular em sua máquina e as dependências:
```bash
npm install
```
Para subir o servidor:
```bash
ng serve
```


