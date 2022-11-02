import os

home_dir = os.getcwd()
# Guarda o diretório raiz

organizar_dir = os.path.join(os.getcwd(), 'Organizar')
# Guarda o caminho da pasta organizar

for i in os.listdir(organizar_dir):
    # Para cada na pasta organizar
    file_dir = os.path.join(organizar_dir, i)
    # Cria um novo caminho nessa pasta
    if os.path.isdir(file_dir) is True:
        # Verifica se o caminho da pasta de extensão é um diretótio
        for file in os.listdir(file_dir):
            os.replace(os.path.join(file_dir, file), os.path.join(home_dir, file))
            # Para cada arquivo, faz um replace, detalhe, o replace precisa apontar para uma pasta + nome do arquivo
            # O primeiro join é a pasta extensão + nome do arquivo
            # O segundo join é a pasta para onde ele vai + nome do arquivo
    os.rmdir(file_dir)
    # Remove a pasta vazia de extensão
os.rmdir(organizar_dir)
# Remove a pasta organizar


# OUTRA FORMA DE FAZER:
# for i in os.listdir():
#     os.chdir(os.getcwd() + '/' + i)
#     # Muda para os diretórios de extensão
#     for x in os.listdir():
#         os.rename(x, f'{home_dir}/{x}')
#     # Move os arquivos, os renomeando para o diretório raiz
#     os.chdir(organizar_dir)
#     # Muda para o diretório de organizar para não dar erro no loop
#     os.rmdir(organizar_dir + '/' + i)
#     # Remove o diretório de extensão
