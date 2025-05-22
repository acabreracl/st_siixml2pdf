# Conversor de DTE XML a PDF y Extractor de Datos SII (Chile)

Este proyecto permite convertir archivos XML de Documentos Tributarios Electrónicos (DTE) chilenos, provenientes del Servicio de Impuestos Internos (SII), a formato PDF. Además, ofrece la capacidad de extraer los datos contenidos en estos archivos XML a una hoja de cálculo Excel.

## Características Principales

A continuación se detallan las funcionalidades más importantes del proyecto:

- **Conversión de XML a PDF:** Convierte archivos DTE XML individuales del SII a formato PDF.
- **Procesamiento por Lotes y Compresión ZIP:** Facilita el procesamiento de múltiples archivos XML DTE. Esto incluye tanto archivos XML "masivos" (aquellos que contienen varios DTEs en un solo XML) como conjuntos de archivos XML individuales. Los archivos PDF resultantes son empaquetados convenientemente en un archivo ZIP para una fácil descarga y manejo.
- **Extracción de Datos a Excel:** Ofrece la funcionalidad de extraer información relevante de los Documentos Tributarios Electrónicos y consolidarla en una hoja de cálculo Excel, facilitando el análisis y la gestión de los datos.
- **Interfaz Web con Streamlit:** Proporciona una interfaz de usuario web, desarrollada con Streamlit, que permite interactuar de manera sencilla e intuitiva con las funciones de conversión y extracción de datos.
- **Manejo de Errores:** Incorpora mecanismos para el manejo de errores, permitiendo identificar y gestionar situaciones donde los archivos XML estén mal formados o presenten algún tipo de problema que impida su correcto procesamiento.

## Estructura de Directorios

Describe brevemente el propósito de los siguientes directorios clave:
- `input/`: Directorio para colocar los archivos XML individuales que se van a convertir.
- `output/pdf/`: Directorio donde se guardan los archivos PDF generados. Los PDFs de conversiones masivas también aparecen aquí antes de ser empaquetados en un ZIP.
- `output/listado_xml.xlsx`: Hoja de cálculo Excel generada con el resumen de los XML procesados (esta es una inferencia basada en el nombre del archivo, verificar si es correcta o si el script `script_obtiene_excel.py` da más pistas).
- `procesados/`: Directorio donde se almacenan los archivos XML que han sido procesados exitosamente (posiblemente en formato ZIP).
- `malos/`: Directorio donde se mueven los archivos XML que generaron errores durante el procesamiento.
- `bulk/`: Directorio utilizado para el procesamiento de archivos XML "masivos". Los archivos subidos mediante la opción masiva en la interfaz Streamlit se guardan aquí temporalmente.
- `templates/`: Contiene las plantillas HTML y CSS (`invoice.html`, `invoice.css`) utilizadas para generar el formato de los PDFs.
- `DTE/`: Módulo que contiene la lógica principal para el parseo e interpretación de los datos de los archivos DTE XML.

## Instrucciones Básicas de Uso

### Interfaz Web (Streamlit)
1.  **Ejecutar la aplicación:** Para iniciar la interfaz web, ejecuta el siguiente comando en tu terminal desde el directorio raíz del proyecto:
    ```bash
    streamlit run xml2pdf.py
    ```
2.  **Conversión Individual:**
    *   En la interfaz, busca la opción "Suba un XML invidual:".
    *   Selecciona y sube tu archivo XML.
    *   Una vez procesado, aparecerá un botón para "Descargar PDF".
3.  **Conversión Masiva:**
    *   Busca la opción "ó suba un XML masivo:".
    *   Sube tu archivo XML que contiene múltiples DTEs o un consolidado.
    *   El sistema procesará cada DTE, generará los PDFs correspondientes y los agrupará en un archivo ZIP.
    *   Aparecerá un botón para "Descargar ZIP" con todos los PDFs.

### Scripts de Línea de Comandos
-   **Conversión por Lotes (`script_convierte_xml.py`):**
    *   Coloca los archivos XML que deseas convertir en el directorio `input/`.
    *   Ejecuta el script: `python script_convierte_xml.py`.
    *   Los PDFs generados se guardarán en `output/pdf/`. Los archivos con errores se moverán a `malos/`.
-   **Generación de Reporte Excel (`script_obtiene_excel.py`):**
    *   Este script (presumiblemente) procesa los XML y genera un archivo Excel (`output/listado_xml.xlsx`) con un resumen de los datos.
    *   Ejecuta el script: `python script_obtiene_excel.py` (Verificar si requiere argumentos o configuración adicional).

## Dependencias

Las dependencias de Python necesarias para este proyecto se encuentran listadas en el archivo `requirements.txt`. Puedes instalarlas utilizando pip:

```bash
pip install -r requirements.txt
```
También existe un archivo `packages.txt`, que podría listar dependencias a nivel de sistema operativo si se utiliza en ciertos entornos o contenedores.

## Módulo DTE

El directorio `DTE/` contiene el módulo principal (`DTE.py`) encargado de analizar (parsear) los archivos XML de los Documentos Tributarios Electrónicos. Esta clase se ocupa de extraer toda la información relevante de los XML, como datos del emisor, receptor, montos, detalles de productos/servicios, impuestos y referencias, facilitando su posterior conversión a PDF y extracción de datos.

## Agradecimientos

Este proyecto se basó inicialmente en el trabajo de **tonicanada**. Puedes encontrar el repositorio original en: [https://github.com/tonicanada/sii_chile_xml_to_pdf](https://github.com/tonicanada/sii_chile_xml_to_pdf).

Se han realizado modificaciones y añadido nuevas funcionalidades como el procesamiento masivo y la interfaz con Streamlit.
