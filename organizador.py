import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione Uma Pasta') # Abre a Biblioteca de Arquivos e Retorna a Pasta Selecionada

lista_arquivos = os.listdir(caminho) # Percorre e Retorna a Lista de Arquivos da Pasta Selecionada

locais = {
    'Imagens':['.png','.jpg','.jpeg','.webp'],
    'PDFs':['.pdf'],
    'Word':['.docx','.log','.txt'],
    'Planilhas':['.xlsx','.csv','.xlsm'],
    'Apresentacoes':['.pptx','.pptm'],
    'Codigos':['.html','.py','.ipynb','.jar','.cpp','.java']
} # Cria as Pastas para Colocar os arquivos no Devido Lugar

outroLocal = 'Outros' # pasta para caso o arquivo não esteja nos formatos/entensões acima

for arquivo in lista_arquivos: # Percorre a lista de Arquivos
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}') # Separa o Nome do Arquivo da Sua Extensão

    realocado = False # verifica se o arquivo já foi realocado ou não

    for pasta in locais: # Percorre os Valores dentro do Dicionario Locais
        if extensao in locais[pasta]:

            if not os.path.exists(f'{caminho}/{pasta}'): # Caso a pasta não exista ele cria uma nova
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') # Caso a extensao esteja presente no Dicionario ele coloca o arquivo na pasta adequada
            realocado = True
            print(f'Novo Caminho: {pasta}/{arquivo}') # Mostra o novo caminho do arquivo
            
            break # após o arquivo ser realocado ele para a repetição
    
    if not realocado: # se o arquivo não pertencer a nenhuma extensão será colocado na pasta 'Outros'
        if not os.path.exists(f'{caminho}/{outroLocal}'): # Caso a pasta não exista ele cria uma nova
            os.mkdir(f'{caminho}/{outroLocal}')
        os.rename(f'{caminho}/{arquivo}', f'{caminho}/{outroLocal}/{arquivo}')