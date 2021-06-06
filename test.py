"""
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

"""
import cv2
import tkinter as tk
from PIL import ImageTk, Image
import winsound
import _thread




def
mainWindow = tk.Tk()
lmain = tk.Label(mainWindow)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('intro.mp4')

def show_frame():
	try:
		ret, frame = cap.read()
		cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img   = Image.fromarray(cv2image).resize((760, 400))
		imgtk = ImageTk.PhotoImage(image = img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(10, show_frame)
	except:
		lmain.destroy()

def play_audio():
	try:
		sound = winsound.PlaySound("intro.wav", winsound.SND_FILENAME)
	except:
		print("ayaya")



_thread.start_new_thread(play_audio, ())
show_frame()

mainWindow.mainloop()  #Starts GUI
"""
import tkinter as tk
from PIL import ImageTk, Image




window = tk.Tk()

window.rowconfigure(0, weight=3, uniform='row')
window.rowconfigure(1, weight=2, uniform='row')
window.rowconfigure(2, weight=2, uniform='row')
window.rowconfigure(3, weight=2, uniform='row')
window.columnconfigure(0, weight=1, uniform="row")



frame_pp = tk.LabelFrame(window, text="pp")
frame_pp.grid(column=0, row=0, sticky="NESW")
frame_ip = tk.LabelFrame(window, text="ip")
frame_ip.grid(column=0, row=1, sticky="NESW")
frame_nom = tk.LabelFrame(window, text="nom")
frame_nom.grid(column=0, row=2, sticky="NESW")
frame_lancer = tk.LabelFrame(window, text="lancer")
frame_lancer.grid(column=0, row=3, sticky="NESW")


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#PP
pp_choix = 0
def pp_choix_selection(nb):
	pp_choix = nb

frame_pp.columnconfigure(0, weight=1, uniform="row")
frame_pp.columnconfigure(1, weight=1, uniform="row")
frame_pp.columnconfigure(2, weight=1, uniform="row")
frame_pp.columnconfigure(3, weight=1, uniform="row")

pp_1_img = Image.open("data/image/pp_1.jpg")
pp_1_img = pp_1_img.resize((200,200))
pp_1_img = ImageTk.PhotoImage(pp_1_img)
boutton_pp_1 = tk.Button(frame_pp, image=pp_1_img, command=lambda:[pp_choix_selection(1)])
boutton_pp_1.grid(column=0, row=0, sticky="NESW")

pp_2_img = Image.open("data/image/pp_1.jpg")
pp_2_img = pp_2_img.resize((200,200))
pp_2_img = ImageTk.PhotoImage(pp_2_img)
boutton_pp_2 = tk.Button(frame_pp, image=pp_2_img, command=lambda:[pp_choix_selection(2)])
boutton_pp_2.grid(column=1, row=0, sticky="NESW")

pp_3_img = Image.open("data/image/pp_1.jpg")
pp_3_img = pp_3_img.resize((200,200))
pp_3_img = ImageTk.PhotoImage(pp_3_img)
boutton_pp_3 = tk.Button(frame_pp, image=pp_3_img, command=lambda:[pp_choix_selection(3)])
boutton_pp_3.grid(column=2, row=0, sticky="NESW")

pp_4_img = Image.open("data/image/pp_a.jpg")
pp_4_img = pp_4_img.resize((200,200))
pp_4_img = ImageTk.PhotoImage(pp_4_img)
boutton_pp_4 = tk.Button(frame_pp, image=pp_4_img, command=lambda:[pp_choix_selection(0)])
boutton_pp_4.grid(column=3, row=0, sticky="NESW")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#IP
frame_ip.columnconfigure(0, weight=1, uniform="row")
frame_ip.columnconfigure(1, weight=3, uniform="row")

tk.Label(frame_ip, text="IP").grid(row=0, column=0, sticky="NESW")
ip_entree = tk.Entry(frame_ip)
ip_entree.grid(row=0, column=1)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#NOM
frame_nom.columnconfigure(0, weight=1, uniform="row")
frame_nom.columnconfigure(1, weight=3, uniform="row")

tk.Label(frame_ip, text="NOM").grid(row=0, column=0, sticky="NESW")
nom_entree = tk.Entry(frame_nom)
nom_entree.grid(row=0, column=1)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#LANCEMENT
frame_lancer.columnconfigure(0, weight=1, uniform="row")
frame_lancer.rowconfigure(0, weight=1, uniform="row")
tk.Button(frame_lancer, text="lancer").grid(row=0, column=0, sticky="NESW")


window.mainloop()













"""
A Faire:
-Popup de win (round/epreuve/all)
-finir menu demarrer
-regler bug menu
-









"""