import os
import shutil

diretorio = '/home/jota/course-python'
os.chdir(diretorio)

for arquivo in os.listdir('.'):
    if arquivo.endswith('.py') and arquivo.startswith('aula'):
        numero_aula = int(''.join(filter(str.isdigit, arquivo)))
        diretorio_destino = f'aula{(numero_aula-1)//10*10+1}-{(numero_aula-1)//10*10+10}'
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)
        shutil.move(arquivo, diretorio_destino)
