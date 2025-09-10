import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'harcascade_frontface_default.xml')

img = cv2.imread('IMG_2974.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

cv2.imshow('Detected Faces', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
