#O programa pede um ano ao usuário e informa se este ano é ou não bissexto.

ano = int(input("Informe o ano: "))

if ano % 100 == 0: #ou seja, se o ano tem final 00
  if ano % 400 == 0: #anos terminados em 00 só são bissextos se forem divisíveis por 400
    print(f"O ano de {ano} é bissexto!")
  else:
    print(f"O ano de {ano} não é bissexto!")
else:
  if ano % 4 == 0: #um ano que não tem final 00 só é bissexto se for múltiplo de 4
    print(f"O ano de {ano} é bissexto!")
  else:
    print(f"O ano de {ano} não é bissexto!")
