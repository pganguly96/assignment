from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import tkinter as tk
# import the necessary packages
from PIL import Image
from PIL import ImageTk
import threading
import datetime
import imutils
import cv2
import os


def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image = Image.fromarray(image)
        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        panelA.grid(row = 0, column = 0)
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            # while the second panel will store the edge map
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelA.image = image
            panelA.after(10, camera)

def camera():
    global panelA, panelB
    global img
    global cap
    _, image = cap.read()
    image = cv2.flip(image, 1)
    img = image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    if panelA is None or panelB is None:
        # the first panel will store our original image
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
        # while the second panel will store the edge map
    # otherwise, update the image panels
    else:
        # update the pannels
        panelA.configure(image=image)
        panelA.image = image


# initialize the window toolkit along with the two image panels
root = tk.Tk()
panelA = tk.Frame(root, width=600, height=100 )
panelB = None
img = None
cap = cv2.VideoCapture(0)
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
btn = Button(root, text="Camera", command=camera)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
#panelA.grid(row = 0, column = 0)
camera()
# kick off the GUI
root.mainloop()