# O programa calcula o fatorial do número fornecido pelo usuário.

def fatorial(n: int) -> int:
  produto = 1
  while n > 0:
    produto *= n
    n -= 1
  return produto

n = int(input("Insira um número: "))
print(fatorial(n))
