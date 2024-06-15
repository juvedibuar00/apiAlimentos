from pydantic import BaseModel
from alimentos import Alimento, alimento1

class BancoDados:
    def __init__(self, objetoDados={}):
        self.dados = objetoDados

    #adicionar um novo alimento
    def adicionarAlimento(self, alimento: Alimento):
        self.dados[alimento.id] = alimento


bd = BancoDados()

alimento2 = Alimento(1, 'teste', 10.50, True, 10, '')

bd.adicionarAlimento(alimento2)

print(bd.dados[2].nome)