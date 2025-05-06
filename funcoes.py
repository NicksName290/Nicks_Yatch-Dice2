#versao : 13
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#maybe, im calm
def guardar_dado(rolados, estoque, guardar):
    lista = []
    estoque.append(rolados[guardar])
    del rolados[guardar]
    lista.append(rolados)
    lista.append(estoque)
    return lista
