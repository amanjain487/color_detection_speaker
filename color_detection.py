import numpy as np
import cv2
import pyttsx3
import csv

engine = pyttsx3.init()

def get_text(colors_list, b,g,r):
    distance = 10000
    color = ""
    for i in colors_list:
        error = abs(int(i[2]) - r) + abs(int(i[3]) - g) + abs(int(i[4]) - b)
        if error < distance:
            distance = error
            color = i[0]

    return "The Color is " + color

def mouse_movement(event, x, y, flags, end_ver):
    cv2.imshow(file_name, image)

    if event == cv2.EVENT_MOUSEMOVE:

        rgb = image[y,x]
        R = rgb[0]
        G = rgb[1]
        B = rgb[2]

        b_hex = str(hex(B))[2:]
        if len(b_hex) == 1:
            b_hex = "0" + b_hex

        g_hex = str(hex(G))[2:]
        if len(g_hex) == 1:
            g_hex = "0" + g_hex

        r_hex = str(hex(R))[2:]
        if len(r_hex) == 1:
            r_hex = "0" + r_hex

        color_code = r_hex + g_hex + b_hex

        color_code = color_code.upper()

        text = "Color_Code = #" + color_code + " R = " + str(R) + " G = " + str(G) + " B = " + str(B)
        print(text)

        cv2.rectangle(image, (0,0), (int(end_ver),40), (int(R),int(G),int(B)), -1)

        if(int(R)+int(G)+int(B)) < 600:
            cv2.putText(image, text, (15,30), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        elif (int(R)+int(G)+int(B)) > 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    if event == cv2.EVENT_LBUTTONDOWN:

        rgb = image[y, x]
        R = int(rgb[0])
        G = int(rgb[1])
        B = int(rgb[2])

        b_hex = str(hex(B))[2:]
        if len(b_hex) == 1:
            b_hex = "0" + b_hex

        g_hex = str(hex(G))[2:]
        if len(g_hex) == 1:
            g_hex = "0" + g_hex

        r_hex = str(hex(R))[2:]
        if len(r_hex) == 1:
            r_hex = "0" + r_hex

        color_code = "#" + r_hex + g_hex + b_hex

        color_code = color_code.upper()

        text = "Color_Code = " + color_code + " R = " + str(R) + " G = " + str(G) + " B = " + str(B)

        cv2.rectangle(image, (0, 0), (int(end_ver), 40), (int(B), int(G), int(R)), -1)

        if (int(R) + int(G) + int(B)) < 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        elif (int(R) + int(G) + int(B)) > 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

        speak_text = get_text(colors_list, int(R), int(G), int(B))

        engine.setProperty('rate', 125)

        engine.say(speak_text)

        engine.runAndWait()
        cv2.imshow(file_name, image)


image_path = "sample_image.jpg"

image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)

image_path = image_path.replace("\\","/")
file_name = image_path.split("/")[-1]
file_name = file_name.split(".")[0]

with open('Colors.csv', newline='') as f:
    reader = csv.reader(f)
    colors_list = list(reader)


end_ver = image.shape[1]
cv2.imshow(file_name, image)
#cv2.rectangle(image, (20,20), (100,60), (0,255,0), -1)

cv2.setMouseCallback(file_name, mouse_movement, end_ver)

while(1):
    cv2.imshow(file_name, image)

    if cv2.waitKey(20) & 0xFF ==27:
        break
