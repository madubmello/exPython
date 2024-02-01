#O programa que recebe um número, calcula e mostra a tabuada (de 1 a 10) desse número.

num = int(input("Insira o número inteiro que deseja saber a tabuada: "))

def tabuada(num: int):
  for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")

tabuada(num)
