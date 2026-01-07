# Recebemos CPFs em formato de texto
# Alguns têm pontos, traços ou espaços extras
# O objetivo é:
# - remover espaços no início e no fim
# - remover pontos e traços
# - manter apenas os CPFs que tenham exatamente 11 dígitos

cpfs = ["123.456.789-00", "11111111111", "222.333.444-5", " 999.888.777-66 "]

# Crie a lista cpfs_ok usando list comprehension
# Resultado esperado:
# ["12345678900", "11111111111", "99988877766"]

def ajusta_cpf(cpf):
    cpf = cpf.strip()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    return cpf

cpfs_ok = [
    cpf_ajustado 
    for cpf in cpfs 
    if len(cpf_ajustado := ajusta_cpf(cpf)) == 11
    ]

print(cpfs_ok)
