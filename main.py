import numpy as np
import cv2
from PIL import ImageGrab
import screen_brightness_control as sbc
import time
from screeninfo import get_monitors

monitor_num = 0

for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')
def mostFrequent(List):
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 
monitor_x = get_monitors()[monitor_num].x
monitor_y = get_monitors()[monitor_num].y
monitor_w = get_monitors()[monitor_num].width
monitor_h = get_monitors()[monitor_num].height
print( monitor_x, monitor_y, monitor_w, monitor_h)
step = 50
num_pixel = monitor_w//step * monitor_h//step
count = 0
while True:
    try:
        img = ImageGrab.grab()
        imgNP = np.array(img)

        im_arr = np.frombuffer(img.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((img.size[1], img.size[0], 3))
        r = g = b = 0
        pixelArray = []
        for y in range(monitor_y, monitor_h, step):
            for x in range(monitor_x, monitor_w, step):
                px = im_arr[y][x]

                pixelArray.append([px[0], px[1], px[2]])

        mostFrequentColor = mostFrequent(pixelArray)
        # print(mostFrequentColor)
        count += 1
        e = round(((((int(mostFrequentColor[0])+int(mostFrequentColor[1])+int(mostFrequentColor[2]))/3)/255))*50)
        # current = sbc.get_brightness(display=sbc.list_monitors()[monitor_num])[0]
        # print(current)
        target = e+50
        sbc.fade_brightness(target, display=sbc.list_monitors()[monitor_num])
    except:
        print("Error, (fell asleep?)")
    time.sleep(0.2)
    #print(count)