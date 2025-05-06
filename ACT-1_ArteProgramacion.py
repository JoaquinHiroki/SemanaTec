import cv2
import numpy as np

imagen = cv2.imread('placa.jpg')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#Filter
filtrada = cv2.bilateralFilter(gris, d=9, sigmaColor=75, sigmaSpace=75)
kernel = np.ones((2, 2), np.uint8)
erosionada = cv2.erode(filtrada, kernel, iterations=1)
canny = cv2.Canny(erosionada, threshold1=40, threshold2=100)
kernel_dilatar = np.ones((2, 2), np.uint8)
bordes_engrosados = cv2.dilate(canny, kernel_dilatar, iterations=1)

#Noise elimination
kernel_apertura = np.ones((3, 3), np.uint8)
bordes_limpios = cv2.morphologyEx(bordes_engrosados, cv2.MORPH_OPEN, kernel_apertura)
fondo = np.full_like(bordes_limpios, 30)  
resultado = cv2.bitwise_or(fondo, bordes_limpios)

#Blur
resultado_blur = cv2.GaussianBlur(resultado, (9, 9), 2)
resultado_final = cv2.addWeighted(resultado, 1.5, resultado_blur, -0.5, 0)

#Results
cv2.imshow("Placa resaltada", resultado_final)
cv2.waitKey(0)
cv2.destroyAllWindows()















