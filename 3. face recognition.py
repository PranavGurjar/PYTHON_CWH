import cv2

#Loading The Cascade File
# Load the Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# #Reading the Input Image
# Load the input image with full path
image = cv2.imread("CWH_Python/Python_Day2/02-Day2-Application-of-Python/3. Face Recognition/1.jpg")
# image = cv2.imread("CWH_Python/Python_Day2/02-Day2-Application-of-Python/3. Face Recognition/1.png")





#Resizing the Image
img = cv2.resize(image,None,fx=0.3,fy=0.3)

#Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()