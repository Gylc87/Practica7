import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
  #HSV HUE, SAT, VALUE AMARILLO
    amarillo_bajo = np.array([15,100,20],np.uint8)
    amarillo_alto = np.array([45,255,255],np.uint8)

    mascara_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    resultado_amarillo = cv2.bitwise_and(frame, frame, mask= mascara_amarillo)


    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mascara_amarillo, kernel, iterations = 1)
    dilation = cv2.dilate(mascara_amarillo, kernel, iterations = 1)

    abierto = cv2.morphologyEx(mascara_amarillo, cv2.MORPH_OPEN, kernel)
    cerrado = cv2.morphologyEx(mascara_amarillo, cv2.MORPH_CLOSE, kernel)

    

    cv2.imshow("Frame", frame)
    #cv2.imshow("Resultado Amarillo", resultado_amarillo)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilatacion ", dilation)
    cv2.imshow("Abierto ", abierto)
    cv2.imshow("Cerrado ", cerrado)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()