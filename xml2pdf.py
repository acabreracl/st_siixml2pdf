import locale
import streamlit as st
import pandas as pd
import numpy as np
from xml_to_pdf_functions import sii_doc_XMLtoPDF
import os
import time
import zipfile

locale.setlocale(locale.LC_ALL, 'es_CL')

st.title('SII XML a PDF')

path = './input'

uploaded_file = st.file_uploader("Suba un XML invidual:", type='xml')
if uploaded_file is not None:
    with open("./input/"+uploaded_file.name, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(uploaded_file.getbuffer())
        try:
            f_out = None
            f_out = open(f'{path}/pdf_single_out.xml', 'w')
            for line in uploaded_file:
                line_clean = line.decode().replace('<DTE version="1.0" >','<DTE xmlns="http://www.sii.cl/SiiDte" version="1.0">')
                line_clean_set = line_clean.replace('<SetDTE>','')
                line_clean_set = line_clean_set.replace('</SetDTE>','')
                f_out.write(line_clean_set)
            if f_out:
                f_out.close()

            archivo = sii_doc_XMLtoPDF(f"{path}/pdf_single_out.xml")
            with open(archivo, "rb") as file:
                archivo_nombre = archivo.replace("./output/pdf/","")
                btn = st.download_button(
                        label="Descargar PDF",
                        data=file,
                        file_name=archivo_nombre,
                        mime="application/pdf"
                    )
        except:
            st.write(f"Error convirtiendo {uploaded_file.name}")

uploaded_file_m = st.file_uploader("ó suba un XML masivo:", type='xml')
i = 1
if uploaded_file_m is not None:
    zip = zipfile.ZipFile('./procesados/'+uploaded_file_m.name+'.zip','a')
    
    with open("./bulk/"+uploaded_file_m.name, "wb") as outfile:
        outfile.write(uploaded_file_m.getbuffer())
        f_out = None
        for line in uploaded_file_m:
            if line.startswith(b'<DTE version'):      # we need a new output file
                title = "xx"+str(i)
                i = i + 1
                if f_out:
                    f_out.close()
                f_out = open(f'{path}/{title}.xml', 'w')
            if f_out:
                line_clean = line.decode('latin-1').replace('<DTE version="1.0" >','<DTE xmlns="http://www.sii.cl/SiiDte" version="1.0">')
                line_clean_set = line_clean.replace('</SetDTE>','')
                f_out.write(line_clean_set)
        if f_out:
            f_out.close()
    
    for filename in os.listdir(path):
        if filename.endswith('.xml'):
            try:
                archivo = sii_doc_XMLtoPDF(f"{path}/{filename}")
                with open(archivo, "rb") as file:
                    archivo_nombre = archivo.replace("./output/pdf/","")
                    
                    st.write(f"Archivo {archivo_nombre} agregado a ZIP")
                    zip.write(archivo, archivo)

            except:
                st.write(f"Error convirtiendo {filename}")
            
            time.sleep(1)
    zip.close()

    
    with open('./procesados/'+uploaded_file_m.name+'.zip', 'rb') as fp:
        btn = st.download_button(
            label="Descargar ZIP",
            data=fp,
            file_name=uploaded_file_m.name+'.zip',
            mime="application/zip"
        )

