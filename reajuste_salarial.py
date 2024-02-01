#O programa recebe um salário qualquer e, de acordo com os critérios abaixo, imprime: o valor pré-reajuste, o percentual e o valor de reajuste, e o novo salário.

# Salários até R$ 280,00 (incluindo): aumento de 20%;
# Salários entre R$ 280,00 e R$700,00: aumento de 15%;
# Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
# Salários de R$ 1500,00 em diante: aumento de 5%

valorSalario = float(input("Insira o valor do seu salário (em reais): "))

if valorSalario <= 280:
  aumento = "20%"
  valorAumento = valorSalario*0.2
elif valorSalario < 700:
  aumento = "15%"
  valorAumento = valorSalario*0.15
elif valorSalario < 1500:
  aumento = "10%"
  valorAumento = valorSalario*0.1
elif valorSalario >= 1500:
  aumento = "5%"
  valorAumento = valorSalario*0.05
else:
  print("Salário inválido!")

novoSalario = valorSalario + valorAumento
print(f"O seu salário de R${valorSalario} sofrerá um aumento de {aumento} (ou seja, de R${valorAumento}), portanto, você passará a receber R${novoSalario}!")
