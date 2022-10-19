import requests
import cv2
import os
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
frequency = 1000  
duration = 1000

URL = "http://maker.ifttt.com/trigger/Object/json/with/key/e2tZjkF4zGlEe9ixiXwq8Bl1HxvIAnAXBzAEkXg4-I3"
cnt=0
while video_capture.isOpened():
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cnt+=1
        if cnt%10==0:
            print('Face Found',end=' ')
            print(requests.get(url = URL),cnt)

    cv2.imshow('Detecting Human', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()