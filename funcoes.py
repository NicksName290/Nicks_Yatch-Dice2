#versao : 14
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#maybe, im calm
def guardar_dado(rolados, estoque, manter):
    lista = []
    estoque.append(rolados[manter])
    del rolados[manter]
    lista.append(rolados)
    lista.append(estoque)
    return lista
#ok...
def remover_dado(rolados, estoque, tirar):
   lista = []
   estoque.append(estoque[tirar])
   del estoque[tirar]
   lista.append(estoque)
   lista.append(rolados)
   return lista
