import math

import cv2

#Быстрая настройка границ цветовых поргов HSV
def nope(x):
    pass

def create_trackbar():
    wName = "Filter"
    param_name = ["T_min","T_max"]
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        cv2.createTrackbar(name,wName,0,255,nope)

def update_trackbar():
    wName = "Filter"
    param_name = ["T_min","T_max"]
    data = []
    cv2.namedWindow(wName,cv2.WINDOW_AUTOSIZE)
    for name in param_name:
        data.append(cv2.getTrackbarPos(name,wName))
    return data

def find_moments(img_for_mom,frame_part_num,h_shag):
    moments = cv2.moments(img_for_mom)
    if moments['m00'] > 100:
        object_center = (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00']+frame_part_num*h_shag)) #x,y
        return object_center

def find_angle(point_ceneter,point_object):
    katet_x,katet_y = point_object[0]-point_ceneter[0],point_ceneter[1]-point_object[1]
    angle = int(math.degrees(math.atan2(katet_x,katet_y)))
    print(f"X_k: {katet_x},Y_k: {katet_y},Angle: {angle}")
    return angle


create_trackbar()

camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)
img_part_list = []
key = -1

while key != 27:
    status,img = camera.read()
    img_result = img.copy()
    data_thresh = update_trackbar()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_filter = cv2.inRange(img_gray,data_thresh[0],data_thresh[1])
    h,w = img_filter.shape[:2]
    c_of_parts = 6
    global_angle,angle_counter = 0,0.0001
    h_shag = int(h//c_of_parts)
    img_part_list.clear()
    for i in range(0,c_of_parts):
        img_part_list.append(img_filter[i*h_shag:i*h_shag+h_shag])
        # cv2.imshow(f"{i}",img_part_list[i])
        object_center = find_moments(img_part_list[i],i,h_shag)
        if object_center is not None:
            angle_normal = find_angle((w//2,h//2),(object_center[0]+1,object_center[1]))
            if object_center[1] < h//2:
                angle_counter += 1
                global_angle = (global_angle + angle_normal)
            # print(type(object_center))
            cv2.circle(img_result,(object_center[0],object_center[1]),4,(0,50,255),-1)
            cv2.putText(img_result, str(angle_normal), (object_center[0]+10,object_center[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 190))
    global_angle = int(global_angle // angle_counter)
    print(f"GLobal: {global_angle},Angle_counter: {angle_counter}")

    cv2.circle(img_result, (w//2,h//2), 6, (255, 50, 0), -1)
    cv2.putText(img_result,str(global_angle),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(50,200,190))
    cv2.imshow("Original",img_gray)
    cv2.imshow("Filter", img_filter)
    cv2.imshow("Result", img_result)
    key = cv2.waitKey(33)

cv2.destroyAllWindows()
