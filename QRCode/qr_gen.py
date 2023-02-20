""" QRCode App GUI
Tkinter based application for the QRCode application
GUI.

"""
#!/usr/bin/env python3
import tkinter as tk
from tkinter import PhotoImage, StringVar, ttk
import qrcode
from PIL import Image, ImageTk


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title("QR Code Generator")
		
		self.data_var = tk.StringVar()


		self.photo = tk.PhotoImage(file="gray.png")
		self.label = ttk.Label(image=self.photo)
		self.label.pack()


		self.data_lbl = ttk.Label(text="DATA")
		self.data_lbl.pack()


		self.input_data = ttk.Entry(self, textvariable=self.data_var)
		self.input_data.pack()


		self.btn = ttk.Button(text="Submit", command=self.txt_submit)
		self.btn.pack()


	def txt_submit(self):
		data=self.data_var.get()
		
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)

		qr.add_data(data)
		qr.make(fit=True)
		self.img = qr.make_image(fill_color="black", back_color="white")

		self.new_photo = ImageTk.PhotoImage(self.img)
		self.data_lbl.config(text=data)
		self.label.config(image=self.new_photo)


if __name__ == "__main__":
	app = App()
	app.mainloop()
