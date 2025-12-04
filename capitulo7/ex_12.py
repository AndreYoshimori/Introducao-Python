# Escreva um jogo da velha para dois jogadores. 
# O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. 
# A cada jogada, verifique se a posição está livre. Verfique também quando um jogador venceu a partida.
# Um jogo da velha pode ser visto como uma lista de três elementos na qual cada elemento é outra lista, também com três elementos.

'''
Exemplo do jogo:

X | 0 | 
--+---+--
  | X | X
--+---+--
  |   | 0

Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posição mapeadas para a mesma posição de seu teclado

7 | 8 | 9
--+---+--
4 | 5 | 6
--+---+--
1 | 2 | 3
'''

matriz = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

jogo_da_velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

numeros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
marcador = 'o'
rodada = 0
venceu = False

print('\nInstruções das teclas:\n')
for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " | " if j < len(matriz[i]) - 1 else "\n")
        print('--+---+--' if i < len(matriz) - 1 else "")

while True:
  print(f'\nJogada do {marcador}')

  jogada = input('\nDigite a casa que deseja jogar: ')

  while not jogada.isnumeric():
      print('\nDigite apenas números.')
      print(f'Apenas as seguintes casas estão livres: {numeros_validos}')
      jogada = input('Digite a casa que deseja jogar: ')
  jogada = int(jogada)

  if jogada not in numeros_validos:
      print(f'\nApenas as seguintes casas estão livres: {numeros_validos}')
      continue

  for i in range(len(numeros_validos)):
      if numeros_validos[i] == jogada:
          del numeros_validos[i]
          break

  for i in range(len(matriz)):
      if jogada in matriz[i]:
          for j in range(len(matriz[i])):
              if matriz[i][j] == jogada:
                  jogo_da_velha[i][j] = marcador

  # Verifica horizontais
  for i in range(len(jogo_da_velha)):
      valores_linha_horizontal = ""
      for j in range(len(jogo_da_velha[i])):
          valores_linha_horizontal += jogo_da_velha[i][j]
      if valores_linha_horizontal == 'ooo' or valores_linha_horizontal == 'xxx':
          venceu = True

  # Verifica verticais
  for i in range(len(jogo_da_velha[0])):
      valores_linha_vertical = ""
      for j in range(len(jogo_da_velha)):
          valores_linha_vertical += jogo_da_velha[j][i]
      if valores_linha_vertical == 'ooo' or valores_linha_vertical == 'xxx':
          venceu = True

  # Verifica diagonais
  valores_diagonal_principal = ""
  valores_diagonal_secundaria = ""

  for i in range(len(jogo_da_velha)):
      valores_diagonal_principal += jogo_da_velha[i][i]
      valores_diagonal_secundaria += jogo_da_velha[i][len(jogo_da_velha) - 1 - i]

  if valores_diagonal_principal == 'ooo' or valores_diagonal_principal == 'xxx':
      venceu = True    
  if valores_diagonal_secundaria == 'ooo' or valores_diagonal_secundaria == 'xxx':
      venceu = True
  
  # Print jogo da velha
  print()
  for i in range(len(jogo_da_velha)):
        for j in range(len(jogo_da_velha[i])):
            print(jogo_da_velha[i][j], end = " | " if j < len(jogo_da_velha[i]) - 1 else "\n")
        print('--+---+--' if i < len(jogo_da_velha) - 1 else "")

  if venceu:
      print(f'{marcador} Venceu o jogo!')
      break

  rodada += 1

  if rodada >= 9:
      print('Empate!')
      break

  if rodada % 2 == 0:
      marcador = 'o'
  else:
      marcador = 'x'