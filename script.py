from PIL import Image
from termcolor import colored
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def converter_imagem_para_ascii(caminho_imagem, largura_ascii, manter_cores):
    imagem = Image.open(caminho_imagem)
    imagem = imagem.convert("RGB")
    
    arte_ascii = ""
    
    largura_original, altura_original = imagem.size
    proporcao_aspecto = altura_original / largura_original * 0.55
    altura_ascii = int(proporcao_aspecto * largura_ascii)
    imagem_redimensionada = imagem.resize((largura_ascii, altura_ascii))
    
    for y in range(altura_ascii):
        for x in range(largura_ascii):
            r, g, b = imagem_redimensionada.getpixel((x, y))
            brilho = (r + g + b) / 3
            caractere = obter_caractere_ascii(brilho)
            cor = obter_cor_ascii(r, g, b, manter_cores)
            arte_ascii += colored(caractere, color=cor)
        
        arte_ascii += "\n"
    
    return arte_ascii


def obter_caractere_ascii(brilho):
    caracteres = '@%#*+=-:. '
    num_caracteres = len(caracteres)
    passo_brilho = 256 / num_caracteres
    indice = int(brilho / passo_brilho)
    return caracteres[indice]


def obter_cor_ascii(r, g, b, manter_cores):
    if manter_cores:
        return None
    else:
        return 'grey' if (r + g + b) / 3 < 128 else None


def obter_tamanho_terminal():
    tamanho = os.get_terminal_size()
    return tamanho.columns, tamanho.lines


def interagir_com_usuario():
    print("=== Conversor de Imagem para ASCII ===")
    
    while True:
        print("\nOpções:")
        print("1. Converter imagem para arte ASCII")
        print("2. Sair")
        
        escolha = input("Digite a opção desejada: ")
        
        if escolha == '1':
            # Cria uma janela para selecionar a imagem
            root = Tk()
            root.withdraw()
            caminho_imagem = askopenfilename(title="Selecione a imagem")
            while not os.path.isfile(caminho_imagem):
                print("Caminho da imagem inválido. Tente novamente.")
                caminho_imagem = askopenfilename(title="Selecione a imagem")
            
            largura_terminal, altura_terminal = obter_tamanho_terminal()
            largura_ascii = min(largura_terminal, 100)
            
            manter_cores = input("Deseja manter as cores originais? (s/n): ")
            while manter_cores.lower() not in ['s', 'n']:
                print("Opção inválida. Tente novamente.")
                manter_cores = input("Deseja manter as cores originais? (s/n): ")
            
            manter_cores = manter_cores.lower() == 's'
            
            arte_ascii = converter_imagem_para_ascii(caminho_imagem, largura_ascii, manter_cores)
            
            print("\nPrévia:")
            print(arte_ascii)
            
            salvar = input("Deseja salvar a arte ASCII em um arquivo? (s/n): ")
            if salvar.lower() == 's':
                nome_arquivo = input("Digite o nome do arquivo: ")
                nome_arquivo = nome_arquivo.strip()
                nome_arquivo = nome_arquivo.replace(" ", "_")
                
                diretorio_script = os.path.dirname(os.path.abspath(__file__))
                caminho_arquivo = os.path.join(diretorio_script, nome_arquivo)
                
                with open(caminho_arquivo, 'w') as arquivo:
                    arquivo.write(arte_ascii)
                print("Arte ASCII salva com sucesso.")
        
        elif escolha == '2':
            break
        
        else:
            print("Opção inválida. Tente novamente.")


# Executa o script
interagir_com_usuario()
