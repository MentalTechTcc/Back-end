from dotenv import load_dotenv
from src.application.controllers.PessoaController import router_pessoa 

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
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

app.include_router(router_pessoa)

@app.get("/")
async def root():
    return {"message": "mentalTech !"}