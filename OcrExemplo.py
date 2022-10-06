import cv2
import pytesseract

# Lendop image com openCV
img = cv2.imread("Capture.PNG")

# Definindo o local que o tesseract esta instalado (OBS: O TESSERACT TEM QUE ESTAR INSTALADO PREVIAMENTE NO SISTEMA.)
# LINK DO TESSERACT : https://github.com/UB-Mannheim/tesseract/wiki  DATA 06/10/22
pytesseract.pytesseract.tesseract_cmd = "W:\Program Files\Tesseract-OCR\Tesseract.exe"

# Utilizando o tesseract para transformar a image em string
result = pytesseract.image_to_string(img)

print(result)
