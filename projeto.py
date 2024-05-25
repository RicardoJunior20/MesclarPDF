import PyPDF2
import os

# Cria um objeto PdfMerger para mesclar os PDFs
merger = PyPDF2.PdfMerger()

# Obtém a lista de arquivos na pasta "arquivos" e ordena-os
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

# Imprime os nomes dos arquivos na pasta (apenas para verificação)
print(lista_arquivos)

# Itera sobre cada arquivo na lista de arquivos
for arquivo in lista_arquivos:
    # Verifica se o arquivo é um arquivo PDF
    if ".pdf" in arquivo:
        # Adiciona o arquivo ao objeto merger para mesclá-lo
        merger.append(f"arquivos/{arquivo}")

# Escreve o PDF mesclado em um novo arquivo chamado "PdfUnificado.pdf"
merger.write("PdfUnificado.pdf")