import random

print("Seja bem-vindo(a) ao jogo! Essa é uma versão básica de Pedra, Papel e Tesoura de três rodadas!")
rodadas = 3
pontosPlayer = 0
pontosComputador = 0
for rodadas in range(1, rodadas+1,1):
  listaJogadas = ["pedra", "papel", "tesoura"]
  jogadaPlayer = input("Faça sua jogada (pedra, papel ou tesoura): ").lower() #O .lower() é utilizado para transformar os caracteres da string em lower caps

  while jogadaPlayer != "pedra" and jogadaPlayer != "papel" and jogadaPlayer != "tesoura":
    print("Jogada inválida!")
    jogadaPlayer = input("Faça sua jogada (pedra, papel ou tesoura): ").lower() # não esquecer de pedir novamente, se não o loop não funcionará!
    
  jogadaComputador = random.choice(listaJogadas)
  print(f"A jogada de seu oponente foi {jogadaComputador}.")

  if jogadaPlayer == jogadaComputador:
    print("Houve um empate!")
  elif jogadaPlayer == "pedra" and jogadaComputador == "tesoura":
    print("Você venceu a rodada!")
    pontosPlayer += 1
  elif jogadaPlayer == "papel" and jogadaComputador == "pedra":
    print("Você venceu a rodada!")
    pontosPlayer += 1
  elif jogadaPlayer == "tesoura" and jogadaComputador == "papel":
    print("Você venceu a rodada!")
    pontosPlayer += 1
  else:
    print("Seu oponente venceu a rodada!")
    pontosComputador += 1

print(f"Player {pontosPlayer} X {pontosComputador} Oponente")

if pontosPlayer > pontosComputador:
  print("Você foi o vencedor final!")
elif pontosPlayer == pontosComputador:
  print("Ninguém venceu o jogo!")
else:
  print("Seu oponente foi o vencedor final!")
