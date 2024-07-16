import cv2
from random import randint
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

while True:
    n,img = camera.read()
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
    if len(markerCorners) > 0:
        for tag in markerCorners:
            # print(len(markerCorners))
            cx,cy = 0,0
            for corn_n in range(0,4):
                print(corn_n)
                # print(cx, cy)
                cx = cx + tag[0][corn_n][0]
                cy = cy + tag[0][corn_n][1]

            cx, cy = int(cx//4), int(cy//4)
            cv2.circle(img,(cx,cy),5,(randint(0,255),randint(0,255),randint(0,255)),-1)
    cv2.imshow("IMG" ,img)
    cv2.waitKey(1)