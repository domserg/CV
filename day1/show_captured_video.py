import cv2

if __name__ == "__main__":
    id = 0  # camera id
    cap = cv2.VideoCapture(id)
    key = -1
    while key != 27:  # Esc
        ret, frame = cap.read()
        if ret:  # Display the resulting frame
            cv2.imshow('frame', frame)
        key = cv2.waitKey(25)
    cap.release()  # When everything done, release the video capture object
    cv2.destroyAllWindows()  # destroy all windows
