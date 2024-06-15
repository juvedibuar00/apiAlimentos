from fastapi import FastAPI
from BancoDados import  bd

app = FastAPI
@app.get('/alimentos/')

def buscarTodosAlimentos():
    resposta = bd.dados
    return {
        'dados': resposta,
        'statusCode': 200
    }


