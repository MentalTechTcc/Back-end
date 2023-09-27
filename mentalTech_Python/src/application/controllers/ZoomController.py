from fastapi import APIRouter, FastAPI, HTTPException, Request, Depends, Query
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from authlib.integrations.starlette_client import OAuth
from httpx import AsyncClient
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
import httpx
import requests
import requests.auth
import secrets

route_zoom = APIRouter(
    prefix="/zoom",
    tags=["zoom"]
)

CLIENT_ID = "1f3IHLSmQg2m9DgaD2fUFQ" 
CLIENT_SECRET = "9nPM2MRyOmV31uYIbltRl72foT3pFC6R"  
REDIRECT_URI = "http://localhost:9091/zoom_callback"  


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


@route_zoom.get('/')
def homepage():
    authorization_url = make_authorization_url()
    return {
        "message": "Autentique-se com o Zoom",
        "authorization_url": authorization_url
    }


# Função para gerar a URL de autorização
def make_authorization_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI
    }
    url = "https://zoom.us/oauth/authorize?" + urllib.parse.urlencode(params)
    return url



@route_zoom.get('/zoom_callback')
async def zoom_callback(request: Request, code:str):
    #code = request.query_params.get('code')
    if code:
        # Agcódigo para solicitar um token de acesso ao Zoom
        access_token = await get_access_token(code)

        return {"access_token": access_token}
    else:
        return {"error": "Código de autorização não encontrado na URL"}
    
# Função para obter o token de acesso usando o código de autorização
async def get_access_token(code):
    async with httpx.AsyncClient() as client:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI
        }
        auth = httpx.BasicAuth(CLIENT_ID, CLIENT_SECRET)
        response = await client.post("https://zoom.us/oauth/token", data=data, auth=auth)
        token_data = response.json()
        access_token = token_data.get("access_token")
        return access_token



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