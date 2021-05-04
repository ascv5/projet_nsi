import socket
import _thread
import tkinter as tk
from PIL import ImageTk, Image
import time
import ast

import tools




class Client():

	def __init__(self):
		pass




	def connect(self, info):
		self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientsocket.connect(("localhost", 6666))
		self.send("add_player"+"§"+str(info))
		_thread.start_new_thread(self.listen, ())
		_thread.start_new_thread(self.commande_cmd, ())


	def listen(self):
		while True:
			r = self.clientsocket.recv(2048)
			r = r.decode()
			r = r.split("|")
			del r[-1]
			for a in r:
				a = a.split("§")
				if a [0] == "ping":
					self.printe("pong")
				elif a[0] == "lancer":
					self.printe("lancement")
					game.lancer()
				elif a[0] == "CONNECTED":
					self.printe("connected (thread : " + a[1] + " )")
				elif a[0] == "epreuve":
					if a[1] == "ep1":
						game.epreuve1(a[2])
				elif a[0] == "new_player":
					game.add_player(a[1])
				else:
					print("Unknow command : " + str(a))


	def send(self, msg):
		print(msg)
		self.clientsocket.send(str(msg+"|").encode())



	def commande_cmd(self):
		while True:
			msg = input(">")
			self.send(str(msg))


	def printe(self, a):
		print(a)
		"""
		try:
			game.log.config(text=str(a))
		except:
			pass
		"""
		#game.log.config(text=str(a))
		b = game.console_log["text"]
		b = b + "\n" + a
		game.console_log.config(text=b)




#||||||||||||||||||||||||||||||||PARTIE GRAPHIQUE||||||||||||||||||||||||||||||||

class Game():

	def __init__(self):
		"""
		///
		///
		variable self : 
		log : Label du texte de la console
		"""
		self.other_player = []
		#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
		self.fenetre = tk.Tk()
		self.hauteur = 562
		self.largeur = 1000
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		self.fenetre.resizable(width=False, height=False)
		global game
		game = self
		#martin: inserstion graphique pc tout#
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)
		self.canvas = tk.Canvas(self.fenetre,width=self.largeur, height=self.hauteur)
		self.image_bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img, tags="IMG")
		self.canvas.pack()

		self.frame_epreuve = tk.LabelFrame(self.fenetre, text="EPREUVE", width=57/100*self.largeur, height=56/100*self.hauteur, bg="red")
		self.frame_epreuve.pack()
		self.frame_epreuve.pack_propagate(0)
		self.window_epreuve = self.canvas.create_window(7.53/100*self.largeur, 12.57/100*self.hauteur, window=self.frame_epreuve, anchor=tk.NW)

		self.frame_joueurs = tk.LabelFrame(self.fenetre, text="JOUEURS", width=19.9/100*self.largeur, height=26.3/100*self.hauteur, bg="blue")
		self.frame_joueurs.pack(expand=True, fill="both")
		self.frame_joueurs.grid_propagate(0)
		self.frame_joueurs.rowconfigure(0, weight=1)
		self.frame_joueurs.rowconfigure(1, weight=1)
		self.frame_joueurs.rowconfigure(2, weight=1)
		self.frame_joueurs.columnconfigure(0, weight=1)
		self.frame_joueurs.columnconfigure(1, weight=1)
		self.frame_joueurs_liste = []
		self.window_joueurs = self.canvas.create_window(74.7/100*self.largeur, 15.48/100*self.hauteur, window=self.frame_joueurs, anchor=tk.NW)

		self.frame_score = tk.LabelFrame(self.fenetre, text="SCORE", width=6.5/100*self.largeur, height=40/100*self.hauteur, bg="green")
		self.frame_score.pack()
		self.window_score = self.canvas.create_window(810.5,264,window=self.frame_score, anchor=tk.NW)
		
		self.fenetre.bind("<KeyPress>", self.actualize)
		#
		#
		#
		self.epreuve_en_cour = None
		self.console()
		tk.mainloop()




	def add_player(self, info):
		info = ast.literal_eval(info)
		self.other_player.append(info)
		self.add_player_frame(info, len(self.other_player)-1)


	def add_player_frame(self, info, nb):
		if nb < 2:
			frame = tk.LabelFrame(self.frame_joueurs)
			frame.grid(row=0, column=nb%2, sticky="nesw")
			label_name = tk.Label(frame, text=info["name"])
			label_name.pack()
			label_ide = tk.Label(frame, text=info["ide"])
			label_ide.pack()
		elif nb < 4:
			frame = tk.LabelFrame(self.frame_joueurs)
			frame.grid(row=1, column=nb%2, sticky="nesw")
			label_name = tk.Label(frame, text=info["name"])
			label_name.pack()
			label_ide = tk.Label(frame, text=info["ide"])
			label_ide.pack()
		elif nb < 6:
			frame = tk.LabelFrame(self.frame_joueurs)
			frame.grid(row=2, column=nb%2, sticky="nesw")
			label_name = tk.Label(frame, text=info["name"])
			label_name.pack()
			label_ide = tk.Label(frame, text=info["ide"])
			label_ide.pack()



	def change_resolution(self, largeur, hauteur):
		self.hauteur = int(hauteur)
		self.largeur = int(largeur)
		#self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		"""
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)
		self.image_bg = self.canvas.itemconfigure(self.image_bg, image=img)
		"""
		"""
		self.canvas.delete(self.image_bg)
		del self.image_bg
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)
		test = self.canvas.create_image(100, 100, anchor=tk.NW, image=img)
		"""
		img1 = Image.open("nsi_computer.PNG")
		img2 = img1.resize((self.largeur, self.hauteur), Image.ANTIALIAS)
		img3 = ImageTk.PhotoImage(img2)
		"""
		self.canvas.delete("IMG")
		self.canvas.create_image(0, 0, anchor=tk.NW, image=img3, tags="IMG")
		self.canvas.pack()
		"""
		self.canvas.itemconfig(self.image_bg, image=img3)
		#coord frame
		self.frame_epreuve.config(width=57/100*self.largeur)
		self.frame_epreuve.config(height=56/100*self.hauteur)
		self.frame_epreuve.place(x=7.53/100*self.largeur, y=12.57/100*self.hauteur)
		self.frame_joueurs.config(width=19.9/100*self.largeur)
		self.frame_joueurs.config(height=26.3/100*self.hauteur)
		self.frame_joueurs.place(x=74.7/100*self.largeur, y=15.48/100*self.hauteur)
		self.frame_score.config(width=6.5/100*self.largeur)
		self.frame_score.config(height=40/100*self.hauteur)
		self.frame_score.place(x=81.05/100*self.largeur, y=46.98/100*self.hauteur)


		#self.canvas.config(height=self.hauteur, width=self.largeur)
		#self.canvas.pack()
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))


	def epreuve1(self, ep1_phrase):
		self.epreuve_en_cour = 1
		self.ep1_phrase = ep1_phrase
		label = tk.Label(self.frame_epreuve, text=str(ep1_phrase))
		label.pack()
		self.ep1_entry = tk.Entry(self.frame_epreuve)
		self.ep1_entry.pack()
		self.ep_time_begin = time.time()




	#||||||||||||||||||||||||||||||||PPPPPPPPPPPPP||||||||||||||||||||||||||||||||




	def lancer(self):
		pass

	def console(self):
		#
		fenetre = tk.Toplevel(self.fenetre)
		fenetre.title("CONSOLE")
		fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		#
		frame_entree = tk.LabelFrame(fenetre, text="entree")
		frame_entree.pack(side=tk.BOTTOM, fill=tk.X)
		frame_console = tk.LabelFrame(fenetre, text="hisotrique")
		frame_console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		#
		frame_console.update()
		self.console_log = tk.Label(frame_console, text="Bienvenue dans la console : \n", bg="red")
		self.console_log.pack(side=tk.TOP, anchor=tk.NW)
		self.console_entree = tk.Entry(frame_entree)
		self.console_entree.pack(anchor="s", fill=tk.X)
		#
		self.console_historique = []
		self.console_historique_nb = 0
		fenetre.bind("<Return>", self.console_tri)
		fenetre.bind("<Up>", self.console_fleche)
		fenetre.bind("<Down>", self.console_fleche)


	def console_tri(self, event):
		msg = self.console_entree.get()
		client.printe(msg)
		a = msg.split(" ")
		if a[0] == "serv":
			client.send(str(" ".join(msg.split(" ")[1:])))
		elif a[0] == "connect":
			client.connect(str(" ".join(msg.split(" ")[1:])))
		elif a[0] == "co":
			client.connect("{'name':'sacha'}")
		elif a[0] == "con":
			client.connect("{'name':'test'}")
		else:
			if a[0] == "resize":
				self.change_resolution(a[1], a[2])
			elif a[0] == "exit_console":
				pass
			else:
				client.printe("Unknow command : " + str(a))
		self.console_entree.delete(0, tk.END)
		self.console_historique.append(msg)


	def console_fleche(self, event):
		print(event)
		print(str(event.keysym == "Up"))
		print(self.console_historique)
		if str(event.keysym) == "Up":
			self.console_historique_nb += -1
		elif str(event.keysym) == "Down":
			self.console_historique_nb += 1
		try:
			self.console_entree.insert(0, self.console_historique[self.console_historique_nb])
		except:
			pass




	def actualize(self, KeyRelease):
		if self.epreuve_en_cour == 1:
			if tools.verif_text(self.ep1_phrase, self.ep1_entry.get()) == True:
				#EPREUVE 1 REUSSI
				temps = time.time() - self.ep_time_begin
				client.send("epreuve_finish§" + str(temps))




client = Client()
Game()


#{"name": "sacha", "autre": 10}


"""
A FAIRE:
RESIZE (fond)
pauffiner console
serv : gérer les deconnection
PREMIERE EPREUVE




Burguer quizz



Geoguessr
mémori

"""