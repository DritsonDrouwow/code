import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y , w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Face Detection - Press q to quit', frame)

    emotional_detector = cv2.CascadeClassifier("test.xml")
    for (angry, disgust, fear, happy, neutral, sad, surpise) in faces:
        if faces == angry:
            print(angry)
        if faces == fear:
            print(fear)
        if faces == happy:
            print(happy)
        if faces == neutral:
            print(neutral)
        if faces == sad:
            print(sad)
        if faces == surpise:
            print(surpise)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
