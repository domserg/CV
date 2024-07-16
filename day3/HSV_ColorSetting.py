import cv2

#Быстрая настройка границ цветовых поргов HSV
def nope(x):
    pass

def create_trackbar():
    wName = "Filter"
    param_name = ["H_min","H_max","S_min","S_max","V_min","V_max"]
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        cv2.createTrackbar(name,wName,0,255,nope)

def update_trackbar():
    wName = "Filter"
    param_name = ["H_min","H_max","S_min","S_max","V_min","V_max"]
    data = []
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        data.append(cv2.getTrackbarPos(name,wName))
    return data

create_trackbar()

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

key = -1
while key != 27:
    status,img = camera.read()
    data_hsv = update_trackbar()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_filter = cv2.inRange(img_hsv,(data_hsv[0],data_hsv[2],data_hsv[4]),
                             (data_hsv[1],data_hsv[3],data_hsv[5]))
    cv2.imshow("Original",img)
    cv2.imshow("Filter", img_filter)
    key = cv2.waitKey(33)

cv2.destroyAllWindows()
