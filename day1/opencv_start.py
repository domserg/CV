import cv2

camera = cv2.VideoCapture(0)

while cv2.waitKey(30)!=ord("q"):
    _, img = camera.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv,(120-10,0,50),(120+10,255,255))
    cv2.imshow("ORIGINAL",img)
    cv2.imshow("RGB", img_rgb)
    cv2.imshow("GREY", img_grey)
    cv2.imshow("HSV", img_hsv)
    cv2.imshow("Mask", mask)
    print(cv2.waitKey(1))