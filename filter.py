import numpy as np
import cv2

img = cv2.imread("lion.jpg")
cv2.imshow("original", img)

kernel = np.array([[0.272, 0.534, 0.131],
                   [0.349, 0.686, 0.168],
                   [0.393, 0.769, 0.189]])

kernel1 = np.array([[0.0030, 0.0133, 0.0219, 0.0133, 0.0030],
                    [0.0133, 0.0596, 0.0983, 0.0596, 0.0133],
                    [0.0219, 0.0983, 0.1621, 0.0983, 0.0219],
                    [0.0133, 0.0596, 0.0983, 0.0596, 0.0133],
                    [0.0030, 0.0133, 0.0219, 0.0133, 0.0030]])

kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
kernel3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel4 = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [-1, -1, -1]])
kernel5 = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])
kernel6 = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
kernel7 = np.array([[-1, -2 ,-1],[0,0,0],[1 ,2 ,1]])
blurred_image = cv2.filter2D(img, -1, kernel1)
cv2.imshow("Blurred", blurred_image)
sepia_image = cv2.filter2D(img, -1, kernel)
cv2.imshow("sepia_image", sepia_image)
edgedet_image = cv2.filter2D(img, -1, kernel2)
cv2.imshow("EDGE DETECTION",edgedet_image)
sharp_image = cv2.filter2D(img, -1, kernel3)
cv2.imshow("SHARPEN",sharp_image)
edge_h_image = cv2.filter2D(img, -1, kernel4)
cv2.imshow("edge_horizontal_image", edge_h_image)
edge_v_image = cv2.filter2D(img, -1, kernel5)
cv2.imshow("edge_vertical_image", edge_v_image)
emboss_image = cv2.filter2D(img, -1, kernel6)
cv2.imshow("EMBOSS",emboss_image)
sbl_image = cv2.filter2D(img, -1, kernel7)
cv2.imshow("SOBEL",sbl_image)
cv2.waitKey(0)





