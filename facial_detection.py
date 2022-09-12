import cv2
import os

os.environ
cap=cv2.VideoCapture("rtsp://username:password@10.3.0.222:554/cam/realmonitor?channel=1&subtype=1")
cap.set(3,640) #width set
cap.set(4,480) #height set
cap.set(10,100)#brigthness set
faceCascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",img)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break



cv2.waitKey(0)
