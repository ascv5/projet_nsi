import socket
import _thread



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
					print("pong")


	def send(self, msg):
		self.clientsocket.send(str(msg+"|").encode())



	def commande_cmd(self):
		while True:
			msg = input(">")
			self.send(msg)





#||||||||||||||||||||||||||||||||PARTIE GRAPHIQUE||||||||||||||||||||||||||||||||

class Game():

	def __init__(self):
		self.fenetre = tk.Tk()


a = Client()
a.connect({"name": "sacha", "autre": 10})


game = Game()