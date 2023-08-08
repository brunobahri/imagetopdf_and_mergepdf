import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_folder, output_pdf_path):
    pdf_paths = [os.path.join(pdf_folder, filename) for filename in os.listdir(pdf_folder) if filename.lower().endswith('.pdf')]
    
    merger = PdfMerger()
    
    for pdf_path in pdf_paths:
        merger.append(pdf_path)
    
    merger.write(output_pdf_path)
    merger.close()

# Caminho da pasta para os PDFs
pdf_folder = 'pdf'

# Caminho do PDF unificado
output_pdf_path = 'unificado/unificado.pdf'

# Unificar PDFs
merge_pdfs(pdf_folder, output_pdf_path)
