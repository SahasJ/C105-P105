import os
import cv2


path = "Images1"

Images1 = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images1.append(file_name)
        
print(len(Images1))
count = len(Images1)

frame = cv2.imread(Images1 = [0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('Video1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(0, count -1):
    frame = cv2.imread(Images1[i])
    out.write(frame)

out.release()
print("done!")