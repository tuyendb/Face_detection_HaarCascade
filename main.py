import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (125, 125, 125), 2)
        cv2.putText(frame, 'Face', (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (125, 125, 125), 2)

    eyes = eyes_cascade.detectMultiScale(gray, 2.3, 4)
    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1), (125, 125, 125), 2)
        cv2.putText(frame, 'Face', (x1, y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (125, 125, 125), 2)
    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()