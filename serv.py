import socket
import _thread
import threading
import time
import ast
import tools

class Client(threading.Thread):
	"""
	class créer pour chaque client est permettant de gerer la partie resau de chaque client
	prend en arguement : ip, port, clientsocket, ide (numero attribué lors de la creation du thread)
	"""
	def __init__(self, ip, port, clientsocket, ide):
		threading.Thread.__init__(self)
		print("+NEW_THREAD : IP : " + ip + "| id : " + str(ide))
		self.clientsocket = clientsocket
		self.ide = ide


	def run(self):
		_thread.start_new_thread(self.listen, ())


	def listen(self):
		#---> TRY
		while True:
			r = self.clientsocket.recv(2048)
			r = r.decode()
			r = r.split("|")
			del r[-1]
			for a in r:
				a = a.split("§")
				if a[0] == "ping":
					print("pong")
					self.send("ping")
				elif a[0] == "add_player":
					print("+NEW_PLAYER : " + str(a[1]))
					jeu.add_player(self.ide, str(a[1]))
					self.send("CONNECTED§"+str(self.ide))
				elif a[0] == "lancer":
					jeu.lancer_game()
				elif a[0] == "get":
					#chantier
					pass
				elif a[0] == "epreuve_finish":
					jeu.fin_epreuve(self.ide)
				elif a[0] == "EXEC":
					exec(str(a[1]))
				else:
					print("commande inconu : " + str(a))
		#print("Connection error with id : " + str(self.ide) + " or in dvp bug")


	def send(self, msg):
		self.clientsocket.send(str(msg+"|").encode())




class BackGame():

	def __init__(self):
		self.joueur = {}


	def add_player(self, ide, info):
		self.joueur[ide] = ast.literal_eval(str(info))
		self.joueur[ide]["ide"] = ide
		self.joueur[ide]["score"] = 0
		print(self.joueur)
		#envoie aux autres joueurs :
		#AUTRE
		for a in range(0, len(client_thread)):
			if a != ide:
				client_thread[a].send("new_player§"+str(self.joueur[ide]))
		#PERSO
		for a, b in self.joueur.items():
			if a != ide:
				client_thread[ide].send("new_player§"+str(b))



	def lancer_game(self):
		print("LANCEMENT")
		for a in client_thread:
			a.send("lancer")

			#a.send("epreuve§ep1§"+ str(tools.choix_phrase())) 
			a.send("epreuve§ep2§"+ str(tools.ep2_choix_question()))
			self.epreuve_en_cour = 2


	def fin_epreuve(self, ide):
		if self.epreuve_en_cour == 2:
			print("Player " + self.joueur[ide]["name"] + "(" + str(ide) + ") win epreuve 2")







jeu = BackGame()

#||||||||||||||||||||||||||||||||CLIENT ACCEPTER||||||||||||||||||||||||||||||||
client_thread = []


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",6666))

ide = 0
print("SERV IS RUNNING")
while True:
	tcpsock.listen(10)
	(clientsocket, (ip, port)) = tcpsock.accept()
	client_thread.append(Client(ip, port, clientsocket, ide))
	client_thread[ide].start()
	ide += 1

