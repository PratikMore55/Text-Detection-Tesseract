import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
img = cv2.imread('testpy.png')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
print(pytesseract.image_to_string(img))
cv2.imshow("Out", img)
cv2.waitKey(0)