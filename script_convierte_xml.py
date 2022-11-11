from xml_to_pdf_functions import sii_doc_XMLtoPDF
import os

path = "./input"

# Genera los pdf a partir de los XML de la carpeta "input" y los guarda en "output/pdf"
for filename in os.listdir(path):
    try:
        if filename.endswith('.xml'):
            sii_doc_XMLtoPDF(f"{path}/{filename}")
        if filename.endswith('.xmx'):
            sii_doc_XMLtoPDF(f"{path}/{filename}")
    except:
        print(f"error convirtiendo {filename}")
        os.system(f"cp {path}/{filename} ./malos/{filename}")
