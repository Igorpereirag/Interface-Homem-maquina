#EQUIPE: IGOR PEREIRA, SAMARA FADIGAS E VITOR TANAN.

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
  nun = input("digite seu ddd")
  nun = str(nun)
  for ddd in ddds:
    if ddd == nun:
      print(ddds[ddd])
