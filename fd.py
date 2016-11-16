import cv2
import numpy as np
 
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

def read():
	img = cv2.imread('test1.jpg')
	img_gray = cv2.imread('test1.jpg',0)
	return img,img_gray

def detect(img,img_gray):
	faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
	img2 = img.copy()
	for (x,y,w,h) in faces:
		cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)

	return img2

def display(img):
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	img,img_gray = read()
	face = detect(img,img_gray)
	out = np.hstack([img,face])
	display(out)

main()