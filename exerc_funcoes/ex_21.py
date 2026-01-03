# Temos uma string com espaços extras
texto = "   Python é legal   "

# Use walrus para:
# - remover os espaços
# - imprimir o texto apenas se ele não estiver vazio

if (t := texto.strip()):
    print(t)