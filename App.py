import cv2

tracker = cv2.TrackerKCF_create()
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Object Tracking", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') : break

roiObject = cv2.selectROI(frame, False)

trackInit = tracker.init(frame, roiObject)
cv2.destroyWindow("ROI selector")

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    ok, track = tracker.update(frame)

    if ok:
        x,y,w,h = map(int, track)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)


    cv2.imshow("Object Tracking", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') : break