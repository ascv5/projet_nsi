# coding: utf-8
import socket
import _thread
import threading
import time
import ast
import random
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
		self.finish = False


	def run(self):
		_thread.start_new_thread(self.listen, ())


	def listen(self):
		#---> TRY
		while self.finish == False:
			try:
				r = self.clientsocket.recv(2048)
			except:
				if self.finish == False:
					print("Connection lost with thread " + str(self.ide))
					print("1111111111111111111111")
					print(self.finish)
					jeu.deco(self.ide)
				else:
					pass
				break
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
				elif a[0] == "deco":
					jeu.deco(a[1])
				elif a[0] == "lancer":
					jeu.lancer_game()
				elif a[0] == "get":
					#chantier
					pass
				elif a[0] == "scoring":
					jeu.scoring(a[1], a[2])
				elif a[0] == "round_finish":
					jeu.fin_round(self.ide)
				elif a[0] == "EXEC":
					exec(str(a[1]))
				else:
					print("commande inconu : " + str(a))
		print("555555555555555555555555555555")
		#print("Connection error with id : " + str(self.ide) + " or in dvp bug")


	def send(self, msg):
		try:
			self.clientsocket.send(str(msg+"|").encode())
		except:
			print("bon tu clc")


	def presend(self):
		try:
			self.clientsocket.send("alive?|".encode())
		except:
			jeu.deco(self.ide)


	def arret(self):
		print("3333333333333333333333333333")
		print("[-]  thread " + str(self.ide))
		self.finish = True
		print("444444444444444444444444")




class BackGame():

	def __init__(self):
		self.joueur = {}
		#


	def presend(self):
		for a in range(0, len(client_thread)):
			try:
				for a in client_thread.keys():
					client_thread[a].presend()
			except:
				pass

	def add_player(self, ide, info):
		self.joueur[ide] = ast.literal_eval(str(info))
		self.joueur[ide]["ide"] = ide
		self.joueur[ide]["score"] = 0
		print(self.joueur)
		#envoie aux autres joueurs :
		#AUTRE
		self.presend()
		for a in client_thread.keys():
			if a != ide:
				client_thread[a].send("new_player§"+str(self.joueur[ide]))
		#PERSO
		for a, b in self.joueur.items():
			if a != ide:
				client_thread[ide].send("new_player§"+str(b))


	def deco(self, ide):
		print("222222222222222222222222222")
		ide = int(ide)
		client_thread[ide].arret()
		print(self.joueur)
		print(client_thread)
		del self.joueur[ide]
		del client_thread[ide]
		print(self.joueur)
		print(client_thread)
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("deco§"+str(ide))




	def scoring(self, ide, nb=1):
		#TRY
		self.joueur[int(ide)]["score"] += int(nb)
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("scoring§"+str(ide)+"§"+str(nb))
		print(self.joueur)


	def lancer_game(self):
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("lancer")
		self.lancer_epreuve()


	def lancer_epreuve(self):
		#TRAVAILLE
		print("LANCEMENT")
		self.epreuve_en_cour = random.randint(1, 3)
		

		self.epreuve_en_cour = 2
		if self.epreuve_en_cour == 1:
			_thread.start_new_thread(self.ep1, ())
		elif self.epreuve_en_cour == 2:
			_thread.start_new_thread(self.ep2, ())


	def ep1(self, nb_round=5):
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("choix_epreuve§"+str(self.epreuve_en_cour))
		#
		self.ep1_liste = []
		nb = 0
		self.ep1_finished = False
		for a in range(0, nb_round):
			print(a)
			self.ep1_Nround()
			while self.ep1_finished ==False:
				pass

	def ep1_Nround(self):
		self.ep1_finished = False
		print("oeoe")
		phrase = str(tools.ep1_choix_phrase())
		while phrase in self.ep1_liste:
			phrase = str(tools.ep1_choix_phrase())

		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("epreuve§ep1§"+ phrase)
			#client_thread[a].send("epreuve§ep1§"+ str(tools.ep2_choix_question()))


	def ep2(self, nb_round=3):
		theme = tools.ep2_choix_theme()
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("choix_epreuve§"+str(self.epreuve_en_cour)+"§"+str(theme[0])+"§"+str(theme[1]))
		#
		self.ep2_liste = []
		self.ep2_finished = False
		print(theme)
		for a in range(0, nb_round):
			print(a)
			self.ep2_Nround(theme)
			while self.ep2_finished ==False:
				pass


	def ep2_Nround(self, theme):
		self.ep2_finished = False
		question = str(tools.ep2_choix_question(theme))
		while question in self.ep2_liste:
			question = str(tools.ep2_choix_question(theme))
		self.presend()
		for a in client_thread.keys():
			client_thread[a].send("epreuve§ep2§"+tools.ep2_choix_question(theme))



	def fin_round(self, ide):
		if self.epreuve_en_cour == 1:
			print("Player " + self.joueur[ide]["name"] + "(" + str(ide) + ") win round of epreuve 1")
			self.ep1_finished = True
		elif self.epreuve_en_cour == 2:
			print("Player " + self.joueur[ide]["name"] + "(" + str(ide) + ") win round epreuve 2")
			self.ep2_finished = True
		for a in client_thread.keys():
			client_thread[a].send("fin_round§"+str(ide))







jeu = BackGame()

#||||||||||||||||||||||||||||||||CLIENT ACCEPTER||||||||||||||||||||||||||||||||
client_thread = {}


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",6666))

ide = 0
print("SERV IS RUNNING")
while True:
	tcpsock.listen(10)
	(clientsocket, (ip, port)) = tcpsock.accept()
	client_thread[ide] = (Client(ip, port, clientsocket, ide))
	client_thread[ide].start()
	print(client_thread)
	ide += 1

