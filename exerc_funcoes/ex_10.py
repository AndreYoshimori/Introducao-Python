# Usando as mesmas listas
# Crie um dicionário apenas com os alunos aprovados
# Considere aprovado quem tem nota >= 7

# Resultado esperado:
# {"Ana": 8.5, "Carlos": 9.0}

alunos = ["Ana", "Bruno", "Carlos"]
notas = [8.5, 6.0, 9.0]

aprovados = {
    aluno: nota 
    for aluno, nota in zip(alunos, notas) 
    if nota >= 7
    }

print(aprovados)