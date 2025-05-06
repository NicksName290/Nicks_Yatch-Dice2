#versao : 20
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
   rolados.append(estoque[tirar])
   del estoque[tirar]
   lista.append(rolados)
   lista.append(estoque)
   return lista
#proximo
def calcula_pontos_regra_simples(l):
    dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for n in l:
        dicionario[n] += n
    return dicionario
#again
def calcula_pontos_soma(l):
  soma = 0
  for pnt in l:
    soma += pnt
  return soma
#...
def calcula_pontos_sequencia_baixa(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista:
         return 15
   return 0
#agora so que mais
def calcula_pontos_sequencia_alta(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista and i+4 in lista:
         return 30
   return 0
