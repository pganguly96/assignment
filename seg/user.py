#!/usr/bin/python3
import inter as MaaKali
import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk, Label
from tkinter import filedialog
import argparse
import datetime
import cv2
import os
import threading



class Application:
    def __init__(self, output_path="./"):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        self.vs = cv2.VideoCapture(0)  # capture video frames, 0 is your default video camera
        self.output_path = output_path  # store output path
        self.current_image = None  # current image from the camera
        self.notOpen = True
        self.root = tk.Tk()  # initialize root window
        self.root.title("Maa Kali")  # set window title
        self.root.attributes('-fullscreen', True)
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.pack(padx=10, pady=10)
        self.root.config(cursor="arrow")
        # create a button, that when pressed, will take the current frame and save it to file
        save = tk.Button(self.root, text="Snapshot!", command=self.take_snapshot)
        save.pack(fill="both", expand=True, padx=10, pady=10)
        open = tk.Button(self.root, text="Open", command=self.select_image)
        open.pack(fill="both", expand=True, padx=10, pady=10)
        live = tk.Button(self.root, text="Live", command=self.live)
        live.pack(fill="both", expand=True, padx=10, pady=10)
        gpio = tk.Button(self.root, text="GPIO", command=None)
        gpio.pack(fill="both", expand=True, padx=10, pady=10)
        gpio1 = tk.Button(self.root, text="GPIO", command=None)
        gpio1.pack(side = tk.LEFT, fill="both", expand=True, padx=10, pady=10)
        btn = tk.Button(self.root, text="Exit", command=self.destructor)
        btn.pack(side = tk.LEFT, fill="both", expand=True, padx=10, pady=10)
        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()
    def saving(self, file):
        MaaKali.function(file)
    def live(self):
        self.notOpen = False
        self.notOpen = True
        self.video_loop()
    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ok, frame = self.vs.read()  # read frame from video stream
        #        frame = cv2.resize(frame, (1500,1000))
        if ok:  # frame captured without any errors
            key = cv2.waitKey(1000)
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image) # convert image for PIL
            # self.current_image= self.current_image.resize([1280,1024],PIL.Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)  # show the image
            # self.root.attributes("-fullscreen",True)
        if self.notOpen:
            self.root.after(1, self.video_loop)  # call the same function after 30 milliseconds

    def take_snapshot(self):
        """ Take snapshot and save it to the file """
        ts = datetime.datetime.now()  # grab the current timestamp
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path
        self.current_image.save(p, "JPEG")  # save image as jpeg file
        #filename = filename[:-4]
        thread = threading.Thread(target=self.saving, args=(filename[:-4],))
        #thread_list.append(thread)
        thread.start()
        #MaaKali.function(filename[:-4])
        print("[INFO] saved {}".format(filename))

    def select_image(self):
        # grab a reference to the image panels
        # open a file chooser dialog and allow the user to select an input
        # image
        self.notOpen = False
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
            #print(path[int(path.rfind('/')):-4])
            #MaaKali.function(path[(int(path.rfind('/')) + 1):-4])
            #print(path[int(path.rfind('/')):-4])
            #self.panel.grid(row=0, column=0)
            # if the panels are None, initialize them
            if self.panel is None:
                # the first panel will store our original image
                self.panel = Label(image=image)
                self.panel.image = image
                self.panel.pack(side="left", padx=10, pady=10)
                # while the second panel will store the edge map
            # otherwise, update the image panels
            else:
                # update the pannels
                self.panel.configure(image=image)
                self.panel.image = image
            thread = threading.Thread(target=self.saving, args=(path[(int(path.rfind('/')) + 1):-4],))
            # thread_list.append(thread)
            thread.start()

    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="./",
                help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())
# start the app
print("[INFO] starting...")
pba = Application(args["output"])
pba.root.mainloop()
