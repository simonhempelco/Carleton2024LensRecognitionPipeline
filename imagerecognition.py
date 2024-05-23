import numpy as np
import cv2
import hsvtuner

img_in = cv2.imread('CarletonLiquidLensImages\IMG_2606(1).JPG') 
small_image = cv2.resize(img_in, (0,0), fx = 0.25, fy = 0.25)
medium_img = cv2.resize(img_in, (0,0), fx = 0.5, fy = 0.5)

threshold = hsvtuner.tune_hsv(small_image)
lower = threshold[0]
upper = threshold[1]

mask = cv2.inRange(medium_img,lower,upper)
imgResult = cv2.bitwise_and(medium_img,medium_img,mask=mask)
img_gray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
