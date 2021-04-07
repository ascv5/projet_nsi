import socket
import _thread
import tkinter as tk
from PIL import ImageTk, Image





class Client():

	def __init__(self):
		pass




	def connect(self, info):
		self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientsocket.connect(("localhost", 5555))
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
				else:
					print("commande inconnu" + str(a))


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
		self.fenetre = tk.Tk()
		self.hauteur = 562
		self.largeur = 1000
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		global game
		game = self
		#martin: inserstion graphique pc tout#
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)
		self.canvas = tk.Canvas(self.fenetre,width=self.largeur, height=self.hauteur)
		self.image_bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
		self.canvas.pack()
		"""
		self.frame_epreuve = tk.LabelFrame(self.fenetre, text="EPREUVE", width=58/100*self.largeur, height=56/100*self.hauteur, bg="white")
		self.frame_epreuve.pack()
		self.window_epreuve = self.canvas.create_window(13*self.hauteur/100, 7*self.largeur/100, window=self.frame_epreuve, anchor=tk.NW)
		"""
		"""
		tk.Label(self.frame_epreuve, text = "grosse bite de cheval").pack()
		self.frame_joueurs = tk.LabelFrame(self.canvas, text="JOUEURS")
		self.frame_joueurs.pack()
		self.frame_score = tk.LabelFrame(self.canvas, text="SCORE")
		self.frame_score.pack()
		"""
		self.console()
		tk.mainloop()



	def change_resolution(self, hauteur, largeur):
		self.hauteur = int(hauteur)
		self.largeur = int(largeur)
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		self.canvas.config(height=self.largeur, width=self.hauteur)
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)
		self.canvas.itemconfig(self.image_bg, image=img)
		print(self.hauteur)



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
		fenetre.bind("<Return>", self.console_tri)


	def console_tri(self, event):
		msg = self.console_entree.get()
		a = msg.split(" ")
		if a[0] == "serv":
			client.send(str(" ".join(msg.split(" ")[1:])))
		elif a[0] == "connect":
			client.connect(str(" ".join(msg.split(" ")[1:])))
		else:
			if a[0] == "change_resolution":
				self.change_resolution(a[1], a[2])
			else:
				printe("Unknow command : " + str(a))



client = Client()
Game()


#{"name": "sacha", "autre": 10}


