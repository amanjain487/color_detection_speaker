# Color Detection and Color Name Player
This code helps the user to fetch the RGB value of any pixel in an image by just hovering over the pixel and also the color name is pronounced on left-click of mouse on a pixel.

## Requirements
1. Python 3.8 or above

### Required Modules
```
1. csv - to open and read csv file containing colors
2. cv2 - read and display image/sample_image
3. pyttsx3 - initalize speech engine(text-to-speech)
```
To install the above packages using pip command in terminal, run the following code in terminal.

- **pip install python-csv**
- **pip install opencv-python**
- **pip install pyttsx3**

## Description
- The RGB values of a pixel are fetched wherever the mouse pointer is pointing to.
- The Text Box is displayed on hovering and when left-button is clicked a sentence is generated by finding the family of a color of pixel and generating a sentence.
- A csv file named "colors.csv" contains a list of colors which fill be used to fetch the color-family of particular pixel.
- Finally, the sentence is played is using pysttx module.
