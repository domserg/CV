from djitellopy import Tello
tello = Tello()
tello.connect()
print(tello.get_battery())
tello.takeoff()
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # 0 - down
pad = tello.get_mission_pad_id()
old_pad = 0
arr = [1, 2, 3, 5, 6, 7, 8, 4]
i = 0
fb = 0
rl = 0
while True:
    if pad != old_pad:
        if arr[i] == pad:
            if pad == 1:
                fb, rl = 20, 0
            elif arr[i] == 2:
                fb, rl = 0, -20
            elif arr[i] == 3:
                fb, rl = -20, 0
            elif arr[i] == 4:
                fb, rl = 0, 20
            elif arr[i] == 5:
                fb, rl = 0, 20
            elif arr[i] == 6:
                fb, rl = -20, 0
            elif arr[i] == 7:
                fb, rl = 0, -20
            elif arr[i] == 8:
                fb, rl = 20, 0
            i += 1
    tello.send_rc_control(rl, fb, 0, 0)
    old_pad = pad
    pad = tello.get_mission_pad_id()
print(tello.get_battery())
tello.disable_mission_pads()
tello.land()
tello.end()
