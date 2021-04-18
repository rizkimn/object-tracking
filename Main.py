import cv2

tracker = cv2.TrackerKCF_create()
cap = cv2.VideoCapture(0)

# keyCode = cv2.waitKey(1) & 0xFF

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Tracking Object", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') : break

boundBox = cv2.selectROI(frame, False)

trackInit = tracker.init(frame, boundBox)
cv2.destroyWindow("ROI selector")

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    isUpdate, track = tracker.update(frame)
    if isUpdate:
        x, y, w, h = map(int, track)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Object Tracked", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') : break

cap.release()
cv2.destroyAllWindows()