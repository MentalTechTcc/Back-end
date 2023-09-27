from fastapi import APIRouter, FastAPI, HTTPException, Request, Depends, Query
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from authlib.integrations.starlette_client import OAuth
from httpx import AsyncClient
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
import secrets
import httpx

route_zoom = APIRouter(
    prefix="/zoom",
    tags=["zoom"]
)

# Informações da sua conta Zoom
CLIENT_ID = "1f3IHLSmQg2m9DgaD2fUFQ"  # Preencha com o seu Client ID do Zoom
CLIENT_SECRET = "9nPM2MRyOmV31uYIbltRl72foT3pFC6R"  # Preencha com o seu Client Secret do Zoom
REDIRECT_URI = "http://localhost:9091/zoom_callback"  # Defina o seu URI de redirecionamento

# Crie um cliente HTTP para fazer solicitações ao Zoom
client = AsyncClient()

# Modelo para a resposta
class ZoomUserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

# Crie um cliente OAuth para autenticação
oauth = OAuth()
oauth.register(
    name="zoom",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    authorize_url="https://zoom.us/oauth/authorize",
    authorize_params=None,
    authorize_prompt=None,
    authorize_response=None,
    authorize_token=None,
    authorize_redirect_uri=None,
    authorize_token_params=None,
    authorize_scope=None,
    authorize_redirect_error=None,
    authorize_refresh_token=None,
    authorize_refresh_token_params=None,
    authorize_issuer=None,
    authorize_client_kwargs=None,
    client_kwargs=None,
    redirect_to=None,
)

# Endpoint para gerar um link de autorização do Zoom
@route_zoom.get('/')
async def homepage(request: Request):
    authorization_url, state = make_authorization_url()
    request.session["oauth_state"] = state
    return {"authorization_url": authorization_url}

def make_authorization_url():
    state = secrets.token_urlsafe(16)
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": state,
    }
    url = "https://zoom.us/oauth/authorize?" + urllib.parse.urlencode(params)
    return url, state

# Rota de retorno do Zoom após a autorização
@route_zoom.get('/zoom_callback')
async def zoom_callback(
    request: Request, 
    code: str = Query(...),  # Captura o código de autorização da URL de retorno
    state: str = Query(...),  # Captura o estado gerado anteriormente
):
    # Verificar se o estado na resposta corresponde ao estado gerado anteriormente
    if state != request.session.get("oauth_state"):
        raise HTTPException(status_code=400, detail="Mismatching state")

    # O código de autorização agora está disponível como `code`
    # Use-o para obter o token de acesso
    access_token = await get_token(code)

    # Agora você possui o "access token" e pode usá-lo para fazer solicitações à API do Zoom em nome do usuário autenticado
    return {"access_token": access_token}

# Função para obter o access token usando o código de autorização
async def get_token(code):
    # Implemente a lógica para obter o access token usando o código de autorização.
    # Você pode usar sua implementação anterior aqui.

    # Exemplo de obtenção do access token usando a biblioteca Authlib
    from authlib.integrations.starlette_client import OAuth
    oauth = OAuth()
    oauth.register(
        name="zoom",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        authorize_url="https://zoom.us/oauth/authorize",
        authorize_params=None,
        authorize_prompt=None,
        authorize_response=None,
        authorize_token=None,
        authorize_redirect_uri=None,
        authorize_token_params=None,
        authorize_scope=None,
        authorize_redirect_error=None,
        authorize_refresh_token=None,
        authorize_refresh_token_params=None,
        authorize_issuer=None,
        authorize_client_kwargs=None,
        client_kwargs=None,
        redirect_to=None,
    )
    
    token = await oauth.zoom.authorize_access_token(code)
    return token["access_token"]



class ZoomMeetingRequest(BaseModel):
    agenda: str
    duration: int
    password: str
    schedule_for: str
    settings: dict
    start_time: str
    timezone: str
    topic: str
    type: int

# Endpoint para criar uma reunião Zoom
class MeetingData(BaseModel):
    agenda: str
    duration: int
    password: str
    schedule_for: str
    start_time: str
    timezone: str
    topic: str
    type: int



@route_zoom.post('/criar_reuniao')
async def create_zoom_meeting(access_token):
    CREATE_MEETING_URL = "https://api.zoom.us/v2/users/me/meetings"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    meeting_data = {
        "agenda": "My Meeting",
        "duration": 60,
        "password": "123456",
        "schedule_for": "sofialennis44@gmail.com",
        "settings": {
            "alternative_hosts": "",
            "auto_recording": "cloud",
            "host_video": True,
            "language_interpretation": {
                "enable": True,
                "interpreters": [
                    {
                        "email": "interpreter@example.com",
                        "languages": "US,FR"
                    }
                ]
            },
            "meeting_authentication": True,
            "mute_upon_entry": False,
            "registration_type": 1,
            "use_pmi": False
        },
        "start_time": "2022-03-25T07:32:55Z",
        "timezone": "America/Los_Angeles",
        "topic": "My Meeting",
        "type": 2
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(CREATE_MEETING_URL, json=meeting_data, headers=headers)
        meeting_info = response.json()

    return meeting_info