import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
total=0

while 1:
    ret, img = cap.read()
    orig = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    key = cv2.waitKey(1) & 0xFF

    # if the `k` key was pressed, write the *original* frame to disk
    # so we can later process it and use it for face recognition
    if key == ord("k"):
        p = os.path.sep.join(["C:/ritesh/projects/myProjects/demoPCS/images/", "{}.png".format(str(total).zfill(5))])
        cv2.imwrite(p, orig)
        total += 1

    # if the `q` key was pressed, break from the loop
    elif key == ord("q"):
        break

print("[INFO] {} face images stored".format(total))
cap.release()
cv2.destroyAllWindows()
