import cv2

#Быстрая настройка границ цветовых поргов HSV


def create_trackbar():
    wName = "Setting"
    param_name = ["H_min","H_max","S_min","S_max","V_min","V_max"]
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        cv2.createTrackbar(name,wName,0,255,nope)

def update_trackbar():
    wName = "Setting"
    param_name = ["H_min","H_max","S_min","S_max","V_min","V_max"]
    data = []
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        data.append(cv2.getTrackbarPos(name,wName))
    return data

create_trackbar()

camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)

key = -1
while key != 27:
    status,img = camera.read()
    img_result = img.copy()
    data_hsv = update_trackbar()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_filter = cv2.inRange(img_hsv,(data_hsv[0],data_hsv[2],data_hsv[4]),
                             (data_hsv[1],data_hsv[3],data_hsv[5]))
    moments = cv2.moments(img_filter)
    print(img_hsv[100,100])
    if moments['m00'] > 1000:
        object_center = (int(moments['m10']/moments['m00']+1),int(moments['m01']/moments['m00']+1))
        # img_result = cv2.bitwise_or(img_result,img_result,mask = img_filter)
        cv2.circle(img_result,object_center,5,(0,50,255),-1)
    cv2.imshow("Original",img)
    cv2.imshow("Filter", img_filter)
    cv2.imshow("Result", img_result)
    key = cv2.waitKey(33)

cv2.destroyAllWindows()
