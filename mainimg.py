import cv2

face_cascade= cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
img= cv2.imread("images/elon.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face= face_cascade.detectMultiScale(gray, 1.1,4)
for(x,y,w,h) in face:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 3)
cv2.imshow("img",img)
cv2.waitKey(0)