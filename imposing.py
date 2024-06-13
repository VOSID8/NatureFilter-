import cv2
import numpy as np
#hello
img1 = cv2.imread('tryp1.jpg')
img2 = cv2.imread('tryp2.jpg')
imgg1=cv2.resize(img1,(500,500))
imgg2=cv2.resize(img2,(500,500))
dst = cv2.addWeighted(imgg1, 0.5, imgg2, 0.7, 0.0)
img_arr = np.hstack((imgg1, imgg2))
cv2.imshow('Input Images',img_arr)
cv2.imshow('Blended Image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()