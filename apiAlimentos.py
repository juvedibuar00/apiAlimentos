from fastapi import FastAPI
from BancoDados import  bd

app = FastAPI()

@app.get("/alimentos/")
def buscarTodosAlimentos():
    resposta = bd.getAlimentos()
    return {
        'dados': resposta,
        'statusCode': 200
    }


@app.get('alimentos/{id}/')

def buscarUmAlimento(id):
    resposta = bd.getAlimento(id)
