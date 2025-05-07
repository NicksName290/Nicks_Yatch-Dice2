#versao : 39
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
#SEQUENCIA BAIXA (nn e poker...)
def calcula_pontos_sequencia_baixa(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista:
         return 15
   return 0
#SEQUENCIA ALTA (poker???)
def calcula_pontos_sequencia_alta(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista and i+4 in lista:
         return 30
   return 0
#Adoro poker btw, mesmo que nn seja poker. FULL HOUSE
def calcula_pontos_full_house(lista):
   dupla = False
   maior_dupla = 0
   trio = False
   maior_trio = 0
   soma = 0
   for i in lista:
      if lista.count(i) == 2:
         dupla = True
         if i > maior_dupla:
            soma -= maior_dupla*2
            maior_dupla = i
            soma += maior_dupla*2
      if lista.count(i) == 3:
         trio = True
         if i > maior_trio:
            soma -= maior_trio*3
            maior_trio = i
            soma += maior_trio*3
   if trio == True and dupla == True:
      return soma
   return 0
#Odeio quando alguem consegue um QUADRA, sempre e porque eles comecaram com uma dupla
def calcula_pontos_quadra(l):
   soma = 0
   sim = False
   for i in l:
      soma += i
      if l.count(i) >= 4:
        sim = True
   if sim == True : 
      return soma
   return 0
#QUINA (Agr ja saiu do Poker)
def calcula_pontos_quina(l):
   for i in l:
      if l.count(i) >= 5:
         return 50
   return 0#versao : 29
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
#SEQUENCIA BAIXA (nn e poker...)
def calcula_pontos_sequencia_baixa(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista:
         return 15
   return 0
#SEQUENCIA ALTA (poker???)
def calcula_pontos_sequencia_alta(lista):
   for i in lista:
      if i+1 in lista and i+2 in lista and i+3 in lista and i+4 in lista:
         return 30
   return 0
#Adoro poker btw, mesmo que nn seja poker. FULL HOUSE
def calcula_pontos_full_house(lista):
   dupla = False
   maior_dupla = 0
   trio = False
   maior_trio = 0
   soma = 0
   for i in lista:
      if lista.count(i) == 2:
         dupla = True
         if i > maior_dupla:
            soma -= maior_dupla*2
            maior_dupla = i
            soma += maior_dupla*2
      if lista.count(i) == 3:
         trio = True
         if i > maior_trio:
            soma -= maior_trio*3
            maior_trio = i
            soma += maior_trio*3
   if trio == True and dupla == True:
      return soma
   return 0
#Odeio quando alguem consegue um QUADRA, sempre e porque eles comecaram com uma dupla
def calcula_pontos_quadra(l):
   soma = 0
   sim = False
   for i in l:
      soma += i
      if l.count(i) >= 4:
        sim = True
   if sim == True : 
      return soma
   return 0
#QUINA (Agr ja saiu do Poker)
def calcula_pontos_quina(l):
   for i in l:
      if l.count(i) >= 5:
         return 50
   return 0
#agora junta tudo aee!! (Eu nn aguento mais)
def calcula_pontos_regra_avancada(l):
   dic = {}
   soma = 0
   for i in l: 
      soma += i
   dic['cinco_iguais'] = calcula_pontos_quina(l)
   dic['full_house'] = calcula_pontos_full_house(l)
   dic['quadra'] = calcula_pontos_quadra(l)
   dic['sem_combinacao'] = calcula_pontos_soma(l)
   dic['sequencia_alta'] = calcula_pontos_sequencia_alta(l)
   dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(l)
   return dic
#Curiosidade: eu passei mais tempo na 1 e na 2 do que todo o resto
#FAZ JOGADA
def faz_jogada(lista, categoria, cartela):
    if categoria in cartela['regra_simples']:
        if cartela['regra_simples'][categoria] == -1:
            numero = int(categoria)
            pontos_simples = numero * lista.count(numero)
            cartela['regra_simples'][numero] = pontos_simples
    elif categoria in cartela['regra_avancada']:
        if cartela['regra_avancada'][categoria] == -1:
            pontos_avancados = calcula_pontos_regra_avancada(lista)
            cartela['regra_avancada'][categoria] = pontos_avancados[categoria]
    return cartela
