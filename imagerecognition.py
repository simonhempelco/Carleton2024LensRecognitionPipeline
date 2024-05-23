import numpy as np
import cv2
import hsvtuner

img_in = cv2.imread('CarletonLiquidLensImages\IMG_1294.jpg') 


negative_in = cv2.imread('CarletonLiquidLensImages\IMG_Negative.jpg')
negative_small = cv2.resize(negative_in, (0,0), fx = 0.125, fy = 0.125)

screw = cv2.bitwise_and(img_in,negative_in)
lens = cv2.bitwise_xor(img_in,screw)

small_lens = cv2.resize(lens, (0,0), fx = 0.125, fy = 0.125)
medium_lens = cv2.resize(lens, (0,0), fx = 0.25, fy = 0.25)

threshold = hsvtuner.tune_hsv(small_lens)
lower = threshold[0]
upper = threshold[1]

mask = cv2.inRange(medium_lens,lower,upper)


img_blur = cv2.GaussianBlur(mask, (3,3), 0) 
edges = cv2.Canny(img_blur, threshold1=100, threshold2=200) # Canny Edge Detection



# Display Canny Edge Detection Image

cv2.imshow("Image Stack", edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
