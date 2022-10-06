import cv2
import pytesseract

# Lendo image com openCV
# Read image with openCV
img = cv2.imread("Capture.PNG")

# Definindo o local que o tesseract esta instalado (OBS: O TESSERACT TEM QUE ESTAR INSTALADO PREVIAMENTE NO SISTEMA.)
# Setting the path where tesseract is installed (Observation: Tesseract must be previously installed in the system.)
# LINK TESSERACT : https://github.com/UB-Mannheim/tesseract/wiki  Date 06/10/22
pytesseract.pytesseract.tesseract_cmd = "W:\Program Files\Tesseract-OCR\Tesseract.exe"

# Utilizando o tesseract para transformar a image em string
# Using tesseract to transform a image into string
result = pytesseract.image_to_string(img)

print(result)
