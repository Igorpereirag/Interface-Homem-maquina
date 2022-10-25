#EQUIPE: IGOR PEREIRA, SAMARA FADIGAS E VITOR TANAN.


#Dicionario cujo os ddds são como chaves assoaciadas as capitais
ddds = {
  "61": "brasilia",
  "71": "salvador",
  "11": "são paulo",
  "21": "rio de janeiro",
  "32": "juiz de fora",
  "19": "campinhas",
  "27": "vitoria",
  "31": "belo horizonte"
}
while True:
  #recebe o ddd do usuario
  nun = input("digite seu ddd")
  #converte o ddd de inteiro para string
  nun = str(nun)
  #vare  o dicionario
  for ddd in ddds:
    # para cada ddd no dicionario igual ao que o usurio digitou
    if ddd == nun:
      #printa  o estado associado a chave/ddd
      print(ddds[ddd])
