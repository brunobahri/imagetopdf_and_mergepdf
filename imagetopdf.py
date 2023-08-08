import os
from PIL import Image

def convert_images_to_pdf(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.lower().endswith('.png')]
    
    for image_path in image_paths:
        img = Image.open(image_path)
        pdf_path = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + '.pdf')
        
        # Calcula o tamanho da imagem para caber na página
        max_width, max_height = 612, 792  # Tamanho da página letter em pontos (1pt = 1/72 inch)
        if img.width > max_width or img.height > max_height:
            ratio = min(max_width / img.width, max_height / img.height)
            new_width = int(img.width * ratio)
            new_height = int(img.height * ratio)
            img = img.resize((new_width, new_height))
        
        img.save(pdf_path, "PDF", resolution=100.0)

# Caminho da pasta que contém as imagens JPG
image_folder = 'images'

# Caminho da pasta para os PDFs
pdf_folder = 'pdf'

# Converter imagens JPG para PDFs no tamanho da página letter (612x792 pontos)
convert_images_to_pdf(image_folder, pdf_folder)
