import math

list1 = [20,20,-20,-20,90,342]

for i in range(len(list1)-1):
    print(f"Y_kat:{list1[i]}, X_kat:{list1[i+1]}")
    print(math.degrees(math.atan2(list1[i],list1[i+1])))