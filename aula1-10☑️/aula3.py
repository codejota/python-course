# Imprime uma única string
print("Olá, mundo!")

# Imprime duas strings separadas por um espaço (padrão)
print("Olá, mundo!", "Estou programando em Python!")

# Imprime duas strings separadas por um traço
print("Olá, mundo!", "Estou programando em Python!", sep="-")

# Imprime duas strings separadas por um traço, seguidas por uma mensagem específica ao final
print("Olá, mundo!", "Estou programando em Python!", sep="-", end=" Fim do programa!")

# Mesma operação anterior, mas adiciona uma nova linha ao final devido ao '\n'
print("Olá, mundo!", "Estou programando em Python!", sep="-", end=" Fim do programa!\n")

# Usando 'file' para direcionar a saída para um arquivo ou outro stream (exemplo não funcional aqui, apenas ilustrativo)
# print("Olá, mundo!", file=meu_arquivo)

# Imprimindo variáveis com strings (a variável deve ser definida anteriormente)
# var = "Python"
# print(f"Estou programando em {var}!")

# Imprime múltiplos itens, incluindo tipos de dados diferentes, separados por espaços (padrão)
# idade = 30
# print("Eu tenho", idade, "anos")

# Usando o argumento 'flush' para forçar a saída imediata do buffer (útil em arquivos ou quando a saída precisa ser imediata)
# print("Processando...", end="", flush=True)
