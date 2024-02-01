#O programa solicita 3 valores, informa se os valores podem formar um triângulo e, se sim, o tipo desse triângulo.

#OBS: três lados formam um triangulo quando a soma de quaisquer dos dois lados é maior que o terceiro.
     
#Equilátero: três lados iguais
#Isósceles: dois lados iguais
#Escaleno: três lados diferentes

l1 = float(input("Insira o primeiro valor: "))
l2 = float(input("Insira o segundo valor: "))
l3 = float(input("Insira o terceiro valor: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
  triangulo = True
else:
  print("Os valores fornecidos não são capazes de formar um triângulo!")

if triangulo == True:
  if l1 == l2 and l2 == l3:
    print("Os valores fornecidos formam um triângulo equilátero!")
  elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Os valores fornecidos formam um triângulo isósceles!")
  else:
    print("Os valores fornecidos formam um triângulo escaleno!")
