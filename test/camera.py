import sys
import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)


while True:
    _, frame = cap.read()
    cv2.imshow("cam", frame)

    if cv2.waitKey(1) &0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break

