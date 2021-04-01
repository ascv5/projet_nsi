import socket
import _thread
import tkinter as tk





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
		b = game.log["text"]
		b = b + "\n" + a
		game.log.config(text=b)




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
		global game
		game = self
		self.console()
		tk.mainloop()




	def lancer(self):
		pass


	def console(self):
		fenetre = tk.Toplevel(self.fenetre)
		fenetre.title("CONSOLE")
		self.log = tk.Label(fenetre, text="Bienvenu dans la console : \n")
		self.log.pack()
		entree = tk.Entry(fenetre)
		entree.pack()
		tk.Button(fenetre, text="send", command=lambda:[self.console_tri(entree.get())]).pack()


	def console_tri(self, msg):
		if msg.split(" ")[0] == "serv":
			client.send(str(" ".join(msg.split(" ")[1:])))



client = Client()
client.connect({"name": "sacha", "autre": 10})
Game()


