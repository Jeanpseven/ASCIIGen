from PIL import Image
from termcolor import colored

def convert_image_to_ascii(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    ascii_art = ""
    
    width, height = image.size
    aspect_ratio = height / width * 0.55
    new_width = 100
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    
    for y in range(new_height):
        for x in range(new_width):
            r, g, b = resized_image.getpixel((x, y))
            character = " "  # Espaço em branco
            
            # Adiciona o caractere com a cor correspondente
            ascii_art += colored(character, color=(r, g, b))
        
        ascii_art += "\n"
    
    return ascii_art

# Solicita o caminho da imagem ao usuário
image_path = input("Digite o caminho da imagem: ")

# Converte a imagem para ASCII art preservando as cores
ascii_art = convert_image_to_ascii(image_path)

# Exibe o ASCII art no terminal
print(ascii_art)
