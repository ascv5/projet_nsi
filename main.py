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
			for a in r:
				a = a.split("§")
				if a [0] == "ping":
					self.printe("pong")


	def send(self, msg):
		self.clientsocket.send(str(msg+"|").encode())



	def commande_cmd(self):
		while True:
			msg = input(">")
			self.send(msg)


	def printe(self, a):
		print(a)
		"""
		try:
			game.log.config(text=str(a))
		except:
			pass
		"""
		#game.log.config(text=str(a))
		b = game.log["text"]
		b = b + "\n" + a
		game.log.config(text=b)




#||||||||||||||||||||||||||||||||PARTIE GRAPHIQUE||||||||||||||||||||||||||||||||

class Game():

	def __init__(self):
		self.fenetre = tk.Tk()
		self.largeur = 562
		self.longueur = 1000
		self.fenetre.geometry(str(self.longueur)+"x"+str(self.largeur))
		global game
		game = self
		self.console()
		#martin: inserstion graphique pc tout#
		img = Image.open("nsi_computer.PNG")
		img = img.resize((self.longueur,self.largeur))
		img = ImageTk.PhotoImage(img)
		self.canvas = tk.Canvas(self.fenetre,width=self.longueur, height=self.largeur)
		self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
		self.canvas.pack()
		
		self.frame_epreuve = tk.LabelFrame(self.fenetre, text="EPREUVE", width=57/100*self.longueur, height=56/100*self.largeur, bg="red")
		self.frame_epreuve.pack()
		self.window_epreuve = self.canvas.create_window(76,70,window=self.frame_epreuve, anchor=tk.NW)

		self.frame_joueurs = tk.LabelFrame(self.fenetre, text="JOUEURS", width=20/100*self.longueur, height=27/100*self.largeur, bg="blue")
		self.frame_joueurs.pack()
		self.window_joueurs = self.canvas.create_window(747,87,window=self.frame_joueurs, anchor=tk.NW)

		self.frame_score = tk.LabelFrame(self.fenetre, text="SCORE", width=6.5/100*self.longueur, height=40/100*self.largeur, bg="green")
		self.frame_score.pack()
		self.window_score = self.canvas.create_window(810.5,264,window=self.frame_score, anchor=tk.NW)

		tk.mainloop()



	def console(self):
		fenetre = tk.Toplevel(self.fenetre)
		fenetre.title("CONSOLE")
		self.log = tk.Label(fenetre, text="Bienvenu dans la console : \n")
		self.log.pack()
		entree = tk.Entry(fenetre)
		entree.pack()
		tk.Button(fenetre, text="send", command=lambda:[client.send(entree.get())]).pack()


	def update_console(self, a):
		self.log.config(text=a)



client = Client()
client.connect({"name": "sacha", "autre": 10})
Game()


