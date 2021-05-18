
import tkinter as tk


def add(nb, color):
	print(color)
	temp_frame = tk.LabelFrame(frame, bg=color, text=str(nb))
	temp_frame.grid(row=nb//2, column=nb%2, sticky="nesw")
	if nb < 2:
		label = tk.Label(temp_frame, text=str(nb))
		label.pack()



color = ["red", "green", "blue", "pink"]
fenetre = tk.Tk()
fenetre.geometry("300x300")
frame = tk.LabelFrame(fenetre, bg="brown")
#frame.pack_propagate(False)
frame.pack(expand=True, fill="both")

frame.rowconfigure(0, weight=1, uniform='row')
frame.rowconfigure(1, weight=1, uniform='row')
frame.columnconfigure(0, weight=1, uniform='row')
frame.columnconfigure(1, weight=1, uniform='row')
for a in range(0, 4):
	add(a, color[a])








tk.mainloop()



"""
	def printe(self, a):
		print(a)
		#game.log.config(text=str(a))
		b = game.console_log["text"]
		b = b + '\n' + a
		game.console_log.config(text=b)

"""


"""
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Dynamically resize background Image")
# open image file
bg = ImageTk.PhotoImage(file="nsi_computer.png")
# create canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH, expand=True)
# place the image inside canvas
canvas.create_image(0, 0, image=bg, anchor='nw')
# resize function for resizing the image
# with proper width and height of root window
def resize_bg(event):
	global bgg, resized, bg2
	# open image to resize it
	bgg = Image.open("nsi_computer.png")
	# resize the image with width and height of root
	resized = bgg.resize((event.width, event.height), Image.ANTIALIAS)
	
	bg2 = ImageTk.PhotoImage(resized)
	canvas.create_image(0, 0, image=bg2, anchor='nw')
# bind resized function with root window
root.bind("<Configure>", resize_bg)
root.mainloop()
"""


