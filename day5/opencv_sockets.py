import os
import socket
import cv2
#____________________________________________________________________________________________________________\
def nope(x):
    pass
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_name = ('192.168.4.1', 80)
server_socket.connect(server_name)
id = 0
cap = cv2.VideoCapture(id, cv2.CAP_DSHOW)
cv2.namedWindow("Full")
cv2.createTrackbar("D","Full",0,5,nope)
key = -1
while key != 27:  # Esc
    ret, frame = cap.read()
    if ret:x
        cv2.imshow('frame', frame)
        # your code
        data = cv2.getTrackbarPos("D","Full")
        data = chr(data)
        server_socket.send(data.encode("utf-8"))    
    key = cv2.waitKey(25)
cap.release()  # When everything done, release the video capture object
cv2.destroyAllWindows()  # des
