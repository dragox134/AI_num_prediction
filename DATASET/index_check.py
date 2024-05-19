import cv2
import os
import time

file = "Dataset/img"
files_in_folder = os.listdir(file)


for i in range (1, 3840+1):

    if f"{i}.jpg" in files_in_folder:
        img = cv2.imread(f"{file}\\{i}.jpg")
        print(f"{i}.jpg")

    else:
        img = cv2.imread(f"{file}\\{i}.png")
        print(f"{i}.png")

    cv2.imshow("img", img)
    cv2.waitKey(1)
    time.sleep(0.1)