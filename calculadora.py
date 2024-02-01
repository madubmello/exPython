#O programa lê 2 números, a operação que o usuário deseja realizar e imprime o resultado, sua paridade e seu sinal.

num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))
op = input("Qual operação você deseja realizar entre os números fornecidos? (+, -, * ou /)")

def operacao(num1: float, num2: float) -> float:
  if op == "+":
    resultado = num1+num2
  elif op == "-":
    resultado = num1-num2
  elif op == "*":
    resultado = num1*num2
  elif op == "/":
    resultado = num1/num2
  else:
    resultado = "Operação não reconhecida!"

  print(resultado)

  if resultado % 2 == 0:
    print("O resultado é par!")
  else:
    print("O resultado é ímpar!")

  if resultado > 0:
    print("O resultado é positivo!")
  elif resultado == 0:
    print("O resultado é neutro!")
  else:
    print("O resultado é negativo!")

operacao(num1,num2)
