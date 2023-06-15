#!/usr/bin/env python3

"""
A simple application that generates a QR code image based on user input and displays it in a GUI.

Dependencies:
- PIL (Python Imaging Library) for image processing
- tkinter for GUI development

The qr_gen module is required and should contain the following functions:
- qr_data_input: Generates the data for the QR code
- gen_png_image: Generates a PNG image of the QR code

The application consists of a graphical window with the following components:
- An image label to display the QR code image
- A data entry field for the user to input data
- A label to display the entered data

When the user enters data in the data entry field and presses Enter, the entered data is displayed in the label,
and a QR code image based on the entered data is generated and displayed in the image label.
"""

from PIL import Image, ImageTk
import tkinter as tk
from get_csv_data import open_csv
from tkinter.simpledialog import askstring
from qr_gen import qr_data_input as qr_data
from qr_gen import gen_png_image as gen_png


class App(tk.Frame):
    def __init__(self, master):
        """
        Initialize the application.

        Args:
            master (tk.Tk): The root window of the application.
        """
        super().__init__(master)
        self.pack()

        # StringVar declaration
        self.entry_data = tk.StringVar()
        self.entry_lbl_data = tk.StringVar()
        self.generator_mode = tk.IntVar() # checkbox menu "Generator"

        # Image object declaration
        self.img_obj = ImageTk.PhotoImage(Image.open("./img.png"))

        # Widget declaration section
        self.image_lbl = tk.Label(image=self.img_obj)
        self.data_entry = tk.Entry(textvariable=self.entry_data)
        self.data_entry.bind('<Key-Return>', self.get_program_mode)
        self.data_lbl = tk.Label(text="PLACEHOLDER FOR DATA", textvariable=self.entry_lbl_data)

        # Create a menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create a "File" menu section
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_qrcode)
        self.file_menu.add_command(label="Save As", command=self.save_qrcode_as)
        self.file_menu.add_command(label="Close", command=self.quit_application)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create a "Mode" menu section
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_checkbutton(label="CSV Search",
                                          variable=self.generator_mode,
                                          )
        
        self.menu_bar.add_cascade(label="Mode", menu=self.options_menu)

        # Widget pack section
        self.image_lbl.pack()
        self.data_entry.pack(pady=(10, 0))
        self.data_lbl.pack()


    def get_program_mode(self, event):
        """
        Callback function to handle the event when the user presses Enter in the data entry field.

        Retrieves the entered data, updates the label text with the data,
        generates a QR code image using the gen_png function,
        and updates the image label with the newly generated image.

        Args:
            event (tk.Event): The event object triggered by the user action.
        """
        
        data = self.entry_data.get()
        mode = self.generator_mode.get()

        if mode == 0:
            self.display_qrcode(data)
        elif mode == 1 & self.search_csv_data(data):
           self.display_qrcode(data)
        else:
            self.display_qrcode("VALUE NOT FOUND")


    def display_qrcode(self, data):
        self.entry_lbl_data.set(data)
        qr_image = gen_png(qr_data(data), data, mode="open")
        img = ImageTk.PhotoImage(qr_image)
        self.image_lbl.configure(image=img)
        self.image_lbl.image = img

    def save_qrcode(self):
        # Saves an image of the QRCode as a .png file under the name of the data
        data = self.entry_data.get()
        gen_png(qr_data(data), data, mode="save")
        self.entry_lbl_data.set("QRCode Saved")

    
    def save_qrcode_as(self):
        # Saves an image of the QRCode as a .png file under a name defined by the user
        data = self.entry_data.get()
        prompt = askstring("Input", "QRcode Name")
        gen_png(qr_data(data), prompt, mode="save")


    def quit_application(self):
        # Custom method to handle the "Quit" menu option
        self.master.destroy()


    def search_csv_data(self, data):
        return data in open_csv("data.csv")  

    
root = tk.Tk()
root.title("QRCode Generator")
myapp = App(root)
myapp.mainloop()
