# Exercício 3.15: Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
# Exiba o total de dias.
cigarros_dia = int(input('Digite quantos cigarros você fuma por dia:'))
anos = int(input('Digite há quantos anos você fuma cigarro: '))
dias_perdidos = anos * 365 * cigarros_dia * 10 / 1440
print(f'Você perdeu {int(dias_perdidos)} dias de vida.')