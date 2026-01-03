# Temos duas listas relacionadas:
# uma com nomes de alunos
# outra com as respectivas notas

alunos = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 6.0, 9.0]

# O objetivo é criar uma lista de strings no formato:
# "Aluno: Nota"

# Resultado esperado:
# ["Ana: 8.5", "Bruno: 6.0", "Carlos: 9.0"]

lista_alunos_notas = [f"{aluno}: {nota}" for aluno, nota in zip(alunos, notas)]

print(lista_alunos_notas)