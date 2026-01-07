# Temos um dicionário com nomes despadronizados
usuarios = {
    "  aNdrÉ  ": "admin",
    " MARIA": "user",
    "joÃO  ": "user"
}

# Crie um novo dicionário onde:
# - os nomes sejam normalizados (strip + title)
# - os valores permaneçam os mesmos

# Resultado esperado:
# {
#   "André": "admin",
#   "Maria": "user",
#   "João": "user"
# }

def ajusta_nome(nome):
    nome = nome.strip().title()
    return nome

usuarios_ok = {
    ajusta_nome(nome): cargo 
    for nome, cargo in usuarios.items()
    }

print(usuarios_ok)
