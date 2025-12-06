import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(face, (75, 75), 30)
        frame[y:y+h, x:x+w] = blur

    cv2.imshow("Real-Time Face Blur", frame)

    if cv2.waitKey(1) == ord('q'):   # Press Q to quit
        break

cap.release()
cv2.destroyAllWindows()
