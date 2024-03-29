import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'
img = cv2.imread('testpy.png')
# img = cv2.imread('test1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # because tesseract supports images only in RGB format
print(pytesseract.image_to_string(img))      # converts image to string/letters
# print(pytesseract.image_to_boxes(img))     # gives the (x,y,width,height) coordinates

hImg,wImg, channels= img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 2)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)
