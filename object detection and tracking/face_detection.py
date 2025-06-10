import cv2 

#cap = cv.VideoCapture(0)
cap = cv2.VideoCapture("[http://your raspberry pi WiFi address]:8091/?action=stream")

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#face_cascade = cv.CascadeClassifier()
# face_cascade.load(r"C:\Users\BKY-LG\anaconda3\envs\aidrone\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")


while(True):
    ret, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3, 4, 0)

    cv2.imshow('Face', frame)

    if cv2.waitKey(10) >= 0:
        break

cap.release()
cv2.destroyAllWindows()