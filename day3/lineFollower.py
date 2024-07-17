import cv2  # import OpenCV library

id = 0
cap = cv2.VideoCapture(id, cv2.CAP_DSHOW)
key = -1
while (key != 27):
    ret, frame = cap.read()
    if ret:  # Display the resulting frame
        cv2.imshow('Frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
        height = mask.shape[0]
        maskH = mask[:height // 2]
        maskL = mask[height // 2 :]
        cv2.imshow("MaskH", maskH)
        cv2.imshow("MaskL", maskL)
        mH = cv2.moments(maskH)
        mcH = int(mH['m10'] / (mH['m00'] + 1)), int(mH['m01'] / (mH['m00'] + 1))
        cv2.circle(frame, mcH, 20, (255, 0, 0), 2)
        mL = cv2.moments(maskL)
        mcL = int(mL['m10'] / (mL['m00'] + 1)), int(mL['m01'] / (mL['m00'] + 1))
        cv2.circle(frame, (mcL[0], mcL[1] + height // 2), 20, (255, 0, 0), 2)
        cv2.imshow("Frame with mc", frame)
    key = cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()  # destroy windows
