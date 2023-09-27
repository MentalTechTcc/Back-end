from dotenv import load_dotenv
from src.application.controllers.PessoaController import router_pessoa 
from src.application.controllers.ProfissionalController import router_profissional
from src.application.controllers.UserController import routerLoginPessoa 
from src.application.controllers.ConsultaController import router_consulta 
from src.application.controllers.AgendaController import router_agenda
from src.application.controllers.RelatorioController import router_relatorio
from src.application.controllers.TematicasPrincipaisController import router_tematicas_principais
from src.application.controllers.EnderecoController import router_endereco
from src.application.controllers.EspecialidadeController import router_especialidade
from src.application.controllers.DicaSaudeController import router_dica_saude
from src.application.controllers.Avaliacao import router_avaliacao
from src.application.controllers.DiagnosticoController import router_diagnostico
from src.application.controllers.ZoomController import route_zoom


load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Adicione o SessionMiddleware à sua aplicação
app.add_middleware(SessionMiddleware, secret_key="sua_chave_secreta", session_cookie="sua_sessao_cookie")


app.include_router(router_pessoa)
app.include_router(routerLoginPessoa)
app.include_router(router_profissional)
app.include_router(router_consulta)
app.include_router(router_agenda)
app.include_router(router_relatorio)
app.include_router(router_tematicas_principais)
app.include_router(router_especialidade)
app.include_router(router_endereco)
app.include_router(router_dica_saude)
app.include_router(router_avaliacao)
app.include_router(router_diagnostico)
app.include_router(route_zoom)



@app.get("/")
async def root():
    return {"message": "mentalTech !"}