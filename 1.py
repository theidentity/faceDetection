import cv2
import numpy as np

# Read
img = cv2.imread('test1.jpg')
img_gray = cv2.imread('test1.jpg',0)

# Display
# cv2.imshow('img',img)
out = np.vstack([img,img])

cv2.imshow('img',out)



cv2.waitKey(0)
cv2.destroyAllWindows()

