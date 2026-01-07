# Usando as mesmas listas de alunos e notas
# Crie uma lista apenas com os nomes dos alunos
# que tiveram nota maior ou igual a 7

# Resultado esperado:
# ["Ana", "Carlos"]

alunos = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 6.0, 9.0]

aprovados = [
    aluno for aluno, nota
    in zip(alunos, notas) 
    if nota >= 7
    ]

print(aprovados)
