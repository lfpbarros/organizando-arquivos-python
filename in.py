import os

dir_atual = os.getcwd()

os.mkdir('Organizar')
# Cria o diretório Organizar
pastas = [i.split('.')[-1] for i in os.listdir() if os.path.isfile(i) is True]
# Criado a lista com list comprehension

# for i in os.listdir():
#     if os.path.isfile(i) is True:
#         pastas.append(i.split('.')[-1])
# Cria uma lista com as pastas que serão criadas sem list comprehension

pastas = set(pastas)
# Remove as duplicadas

for i in pastas:
    os.mkdir(f'Organizar/{i}')
# Cria as pastas para organizar os arquivos

for i in os.listdir():
    if os.path.isfile(i) is True:
        extensao = i.split('.')[-1]
        if extensao != 'py': # poderia ter usado o in: if '.py' not in i:
            os.rename(i, f'Organizar/{extensao}/{i}')
            # Poderia ser usado o replace, no replace, passamos o caminho atual e o futuro
# Move os arquivos, os renomeando, evitando os .py
