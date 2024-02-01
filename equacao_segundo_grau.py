#O programa pede os valores de A, B e C, e calcula a equação de segundo grau de acordo com os dados fornecidos.

#OBS: se o usuário informar que A=0, a equação não é do segundo grau e o programa não pede os demais valores e se encerra;
#     se o delta for negativo, a equação não possui raízes reais, portanto o programa informa o usuário e se encerra;
#     se o delta for igual a zero, a equação possui apenas uma raiz real, que o programa informará ao usuário;
#     se o delta for positivo, a equação possui duas raízes reais, que o programa informará ao usuário.

import math

a = float(input("Insira o valor de A: "))

if a == 0:
  print("Essa não é uma equação do segunda grau!")
else:
  b = float(input("Insira o valor de B: "))
  c = float(input("Insira o valor de C: "))

  delta = (b**2) - 4*a*c

  if delta < 0:
    print("A equação não possui raízes reais!")
  elif delta == 0:
    raiz = (-b)/2*a
    print(f"Essa equação possui apenas uma raíz real, que é {raiz}.")
  else:
    raiz1 = ((-b)+(math.sqrt(delta)))/2*a
    raiz2 = ((-b)-(math.sqrt(delta)))/2*a
    print(f"Essa equação possui duas raízes reais, que são {raiz1} e {raiz2}.")
