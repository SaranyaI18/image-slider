from itertools import cycle
import tkinter as tk


class App(tk.Tk):
    # Tk window adjusts the size of image

    def __init__(self, image_files, x, y, delay):

        tk.Tk.__init__(self)
         #self variable represents the instance of the object

        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
          #photoimage class is used to display images


        self.pictures_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):

        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)

        self.title(img_name)
        self.after(self.delay, self.show_slides)
         #after method calls a specified function after given delay in ms


    def run(self):
        self.mainloop()
          #mainloop method used when you are ready for application to run.

delay = 3500

image_files = [

    'img1.gif',
    'img2.gif',
    'img3.gif',
    'img4.gif',
    'img5.gif',
    'img6.gif',
    'img7.gif'
]

x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()
