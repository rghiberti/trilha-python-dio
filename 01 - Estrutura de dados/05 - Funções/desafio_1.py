# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.

if quantidade_passos < 0:
  print(f"A quantidade de passos não pode ser",quantidade_passos,"tente novamente com um número positivo")
  
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
elif quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")

# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
else:
  for passos in range(1,quantidade_passos+1):
    if passos == 1:
      print(f"Explorador: ",passos," passo")
    else:
      print(f"Explorador: ",passos," passos")
