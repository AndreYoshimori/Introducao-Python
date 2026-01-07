# Temos duas listas relacionadas:
# uma com nomes de alunos
# outra com as notas correspondentes

alunos = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 6.0, 9.0]

# Crie um dicionário onde:
# - a chave seja o nome do aluno
# - o valor seja a nota

# Resultado esperado:
# {"Ana": 8.5, "Bruno": 6.0, "Carlos": 9.0}

boletim = {aluno: nota for aluno, nota in zip(alunos, notas)}

print(boletim)
