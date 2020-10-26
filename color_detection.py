import cv2
import pyttsx3
import csv

#initialize speech engine
engine = pyttsx3.init()

#function to create a sentence which will be played on left-click
#based on RGB values, a color will be selected from csv file 
def get_text(colors_list, b,g,r):
    distance = 10000
    color = ""
    for i in colors_list:
        error = abs(int(i[2]) - r) + abs(int(i[3]) - g) + abs(int(i[4]) - b)
        if error < distance:
            distance = error
            color = i[0]
    return "The Color is " + color


#function to perform certain operations based on mouse click event
#The operations that can be performed are
#1.Display RGB Values
#2. Determine the family of a colour based on RGB Values and play that name.
def mouse_movement(event, x, y, flags, end_ver):
    cv2.imshow(file_name, image)

    #if mouse_event is hovering
    #Fetch RGB values and display them along with name of family of colour
    if event == cv2.EVENT_MOUSEMOVE:

        #getting the RGB values
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

        #finding color code in HEX
        color_code = r_hex + g_hex + b_hex

        color_code = color_code.upper()

        #generate text to be displayed while Hovering
        text = "Color_Code = #" + color_code + " R = " + str(R) + " G = " + str(G) + " B = " + str(B)
        print(text)

        #create box in which text is to be displayed
        cv2.rectangle(image, (0,0), (int(end_ver),40), (int(R),int(G),int(B)), -1)

        if(int(R)+int(G)+int(B)) < 600:
            cv2.putText(image, text, (15,30), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        elif (int(R)+int(G)+int(B)) > 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    #if mouseevent is left_click
    #fetch RGB Values
    #find the colour name
    #Create sentence and play it using pyttsx engine
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

        #find colour code in HEX
        color_code = "#" + r_hex + g_hex + b_hex

        color_code = color_code.upper()

        text = "Color_Code = " + color_code + " R = " + str(R) + " G = " + str(G) + " B = " + str(B)

        cv2.rectangle(image, (0, 0), (int(end_ver), 40), (int(B), int(G), int(R)), -1)

        if (int(R) + int(G) + int(B)) < 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        elif (int(R) + int(G) + int(B)) > 600:
            cv2.putText(image, text, (15, 30), 2, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

        #text to be spoken is generated using "get_text" function
        #the below function finds the name of colour and also creates sentence to be spoken.
        speak_text = get_text(colors_list, int(R), int(G), int(B))

        #setting the properties of the engine like rate, voice and so on
        engine.setProperty('rate', 125)
        
        #play the generated sentence
        engine.say(speak_text)

        engine.runAndWait()
        cv2.imshow(file_name, image)


        
#beginning of execution
#path of image file
image_path = "sample_image.jpg"

#read/load the image file
image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)

#modify file path to get only file_name
image_path = image_path.replace("\\","/")
file_name = image_path.split("/")[-1]
file_name = file_name.split(".")[0]

#load the csv file with all colors so to check and compare the RGB values and find the family of colour
with open('Colors.csv', newline='') as f:
    reader = csv.reader(f)
    colors_list = list(reader)


end_ver = image.shape[1]

cv2.imshow(file_name, image)
#cv2.rectangle(image, (20,20), (100,60), (0,255,0), -1)

#event checker that detects any mouse events and performs displaying or playing based on mouse event.
cv2.setMouseCallback(file_name, mouse_movement, end_ver)

#infinte while loop which exits when "esc" key is pressed.
while(1):
    cv2.imshow(file_name, image)

    if cv2.waitKey(20) & 0xFF ==27:
        break
