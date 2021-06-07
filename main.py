# coding: utf-8
import socket
import _thread
import tkinter as tk
from PIL import ImageTk, Image
import time
import ast
import cv2
import winsound

import tools




class Client():

	def __init__(self):
		pass




	def connect(self, info, ip):
		self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clientsocket.connect((ip, 6666))
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
					self.printe("pong", inpute=True)
				elif a[0] == "lancer":
					self.printe("lancement", inpute=True)
					game.lancer()
				elif a[0] == "CONNECTED":
					game.setup_game()
					self.printe("connected (thread : " + a[1] + " )", inpute=True)
					self.ide = a[1]
				elif a[0] == "deco":
					game.deco(a[1])
				elif a[0] == "scoring":
					game.scoring(a[1], a[2])
				elif a[0] == "choix_epreuve":
					if a[1] == "1":
						game.epreuve1()
					elif a[1] == "2":
						game.epreuve2(a[2], a[3])
				elif a[0] == "fin_round":
					game.fin_round(a[1])
				elif a[0] == "epreuve":
					if a[1] == "ep1":
						game.ep1_Nround(a[2])
					elif a[1] == "ep2":
						game.ep2_Nround(a[2],a[3])
				elif a[0] == "new_player":
					game.add_player(a[1])
				else:
					self.printe("Unknow command : " + str(a), error=True)



	def send(self, msg):
		print(msg)
		self.clientsocket.send(str(msg+"|").encode())



	def commande_cmd(self):
		while True:
			msg = input(">")
			self.send(str(msg))


	def printe(self, a, error=False, inpute=False, output=False):
		print(a)
		if error == True:
			tk.Label(game.frame_console, text=a, fg="red", bg="black").pack(anchor="nw")
		elif inpute == True:
			tk.Label(game.frame_console, text=a, fg="green", bg="black").pack(anchor="nw")
		elif output == True:
			tk.Label(game.frame_console, text=a, fg="blue", bg="black").pack(anchor="nw")
		else:
			tk.Label(game.frame_console, text=a, fg="white", bg="black").pack(anchor="nw")


#||||||||||||||||||||||||||||||||PARTIE GRAPHIQUE||||||||||||||||||||||||||||||||

class Game():

	def __init__(self):
		global game
		game = self

		self.score = 0
		self.ide = None
		"""
		///
		///
		variable self : 
		log : Label du texte de la console
		"""
		self.other_player = {}
		#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
		self.fenetre = tk.Tk()
		self.hauteur = 562
		self.largeur = 1000
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		self.fenetre.resizable(width=False, height=False)



		self.intro()
		#self.setup_pregame()
		print("test")
		#
		#
		#
		self.epreuve_en_cour = None


		#
		tk.Label(self.fenetre, text="0.1", bg="grey", fg="white").place(x=0, y=0)
		self.console()
		tk.mainloop()


	def intro(self):
		self.intro_lmain = tk.Label(self.fenetre)
		self.intro_lmain.grid(row=0, column=0)
		self.intro_cap = cv2.VideoCapture('data/intro/intro.mp4')
		_thread.start_new_thread(self.intro_play_audio, ())
		self.intro_show_frame()
		print("aaaaaaaaaa")
		#self.intro_lmain.destroy()


	def intro_show_frame(self):
		try:
			ret, frame = self.intro_cap.read()
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image).resize((self.largeur, self.hauteur))
			imgtk = ImageTk.PhotoImage(image=img)
			self.intro_lmain.imgtk = imgtk
			self.intro_lmain.configure(image=imgtk)
			self.intro_lmain.after(10, self.intro_show_frame)
		except:
			self.intro_lmain.destroy()
			self.setup_pregame()


	def intro_play_audio(self):
		try:
			sound = winsound.PlaySound("data/intro/intro.wav", winsound.SND_FILENAME)
		except:
			print("sound error")



	def setup_pregame(self):
		global pp_1_img, pp_2_img, pp_3_img, pp_4_img
		self.pregame_frame = tk.Frame(self.fenetre)
		self.pregame_frame.pack()

		self.pregame_frame.rowconfigure(0, weight=3, uniform='row')
		self.pregame_frame.rowconfigure(1, weight=2, uniform='row')
		self.pregame_frame.rowconfigure(2, weight=2, uniform='row')
		self.pregame_frame.rowconfigure(3, weight=2, uniform='row')
		self.pregame_frame.columnconfigure(0, weight=1, uniform="row")
		
		
		
		frame_pp = tk.LabelFrame(self.pregame_frame, text="pp")
		frame_pp.grid(column=0, row=0, sticky="NESW")
		frame_ip = tk.LabelFrame(self.pregame_frame, text="ip")
		frame_ip.grid(column=0, row=1, sticky="NESW")
		frame_nom = tk.LabelFrame(self.pregame_frame, text="nom")
		frame_nom.grid(column=0, row=2, sticky="NESW")
		frame_lancer = tk.LabelFrame(self.pregame_frame, text="lancer")
		frame_lancer.grid(column=0, row=3, sticky="NESW")
		
		
		#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		#PP
		self.pp_choix = 0
		
		frame_pp.columnconfigure(0, weight=1, uniform="row")
		frame_pp.columnconfigure(1, weight=1, uniform="row")
		frame_pp.columnconfigure(2, weight=1, uniform="row")
		frame_pp.columnconfigure(3, weight=1, uniform="row")

		pp_1_img = Image.open("data/image/pp_1.jpg")
		print(pp_1_img)
		pp_1_img = pp_1_img.resize((int(1000*(3*self.hauteur/10)/740),int((3*self.hauteur/10))))
		print(pp_1_img)
		pp_1_img = ImageTk.PhotoImage(pp_1_img)
		print(pp_1_img)
		boutton_pp_1 = tk.Button(frame_pp, image=pp_1_img, command=lambda:[self.pp_choix_selection(1)])
		boutton_pp_1.grid(column=0, row=0, sticky="NESW")

		pp_2_img = Image.open("data/image/pp_1.jpg")
		pp_2_img = pp_2_img.resize((int(1000*(3*self.hauteur/10)/740),int((3*self.hauteur/10))))
		pp_2_img = ImageTk.PhotoImage(pp_2_img)
		boutton_pp_2 = tk.Button(frame_pp, image=pp_2_img, command=lambda:[self.pp_choix_selection(2)])
		boutton_pp_2.grid(column=1, row=0, sticky="NESW")
		
		pp_3_img = Image.open("data/image/pp_1.jpg")
		pp_3_img = pp_3_img.resize((int(1000*(3*self.hauteur/10)/740),int((3*self.hauteur/10))))
		pp_3_img = ImageTk.PhotoImage(pp_3_img)
		boutton_pp_3 = tk.Button(frame_pp, image=pp_3_img, command=lambda:[self.pp_choix_selection(3)])
		boutton_pp_3.grid(column=2, row=0, sticky="NESW")
		
		pp_4_img = Image.open("data/image/pp_a.jpg")
		pp_4_img = pp_4_img.resize((int(1000*(3*self.hauteur/10)/740),int((3*self.hauteur/10))))
		pp_4_img = ImageTk.PhotoImage(pp_4_img)
		boutton_pp_4 = tk.Button(frame_pp, image=pp_4_img, command=lambda:[self.pp_choix_selection(0)])
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
		
		tk.Label(frame_nom, text="NOM").grid(row=0, column=0, sticky="NESW")
		nom_entree = tk.Entry(frame_nom)
		nom_entree.grid(row=0, column=1)
		#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		#LANCEMENT
		frame_lancer.columnconfigure(0, weight=1, uniform="row")
		frame_lancer.rowconfigure(0, weight=1, uniform="row")

		tk.Button(frame_lancer, text="lancer", command=lambda:[client.connect("{'name':'sacha'}", ip_entree.get( ))]).grid(row=0, column=0, sticky="NESW")


		#MENU
		menu_bare = tk.Menu(self.fenetre)
		#
		menu_view = tk.Menu(menu_bare)
		menu_view.add_checkbutton(label="Fullscreen", command=self.fullscreen)
		#
		self.menu_size_nat = tk .BooleanVar()
		self.menu_size_nat.set(False)
		self.menu_size_size = tk.IntVar()
		self.menu_size_size.set(self.largeur)

		menu_size = tk.Menu(menu_view)
		menu_size.add_checkbutton(label="848x480", onvalue=848, offvalue=not 848, variable=self.largeur, command=lambda:[self.change_resolution("848",  "480")])
		menu_size.add_checkbutton(label="1000x562", onvalue=1000, offvalue=not 1000, variable=self.largeur, command=lambda:[self.change_resolution("1000",  "562")])
		menu_size.add_checkbutton(label="1280x720", onvalue=1280, offvalue=not 1280, variable=self.largeur, command=lambda:[self.change_resolution("1280",  "720")])
		menu_size.add_checkbutton(label="1920x1080", onvalue=1920, offvalue=not 1080, variable=self.largeur, command=lambda:[self.change_resolution("1920",  "1080")])
		menu_size.add_checkbutton(label="Native ("+str(self.fenetre.winfo_screenwidth())+"x"+str(self.fenetre.winfo_screenheight())+")", onvalue=True, offvalue=False, variable=self.menu_size_nat, command=lambda:[self.change_resolution(str(self.fenetre.winfo_screenwidth()), str(self.fenetre.winfo_screenheight()), nat=True)])
		menu_view.add_cascade(menu=menu_size, label="Resolution")

		menu_bare.add_cascade(menu=menu_view, label="MAIN")
		self.fenetre.config(menu=menu_bare)
		self.fullscreen_state = False

		self.fenetre.bind("<KeyPress>", self.actualize)


	def pp_choix_selection(self, nb):
		self.pp_choix = nb

	def setup_game(self):
		#clear
		for widgets in self.pregame_frame.winfo_children():
			widgets.destroy()
		self.pregame_frame.destroy()
		self.fenetre.update()
		#
		img = Image.open("data/image/nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur))
		img = ImageTk.PhotoImage(img)

		self.canvas = tk.Canvas(self.fenetre,width=self.largeur, height=self.hauteur)
		self.canvas.pack()
		self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

		self.frame_epreuve = tk.LabelFrame(self.fenetre, text="EPREUVE", width=57/100*self.largeur, height=56/100*self.hauteur, bg="red")
		self.frame_epreuve.pack()
		self.frame_epreuve.pack_propagate(0)
		self.window_epreuve = self.canvas.create_window(7.53/100*self.largeur, 12.57/100*self.hauteur, window=self.frame_epreuve, anchor=tk.NW)

		self.frame_joueurs = tk.Frame(self.fenetre, width=19.9/100*self.largeur, height=26.3/100*self.hauteur, bg="blue")
		self.frame_joueurs.pack(fill="both")
		self.frame_joueurs.grid_propagate(0)
		self.frame_joueurs.rowconfigure(0, weight=1, uniform='row')
		self.frame_joueurs.rowconfigure(1, weight=1, uniform='row')
		#self.frame_joueurs.rowconfigure(2, weight=1)
		self.frame_joueurs.columnconfigure(0, weight=1, uniform='row')
		self.frame_joueurs.columnconfigure(1, weight=1, uniform='row')
		self.frame_joueurs_liste = []
		self.window_joueurs = self.canvas.create_window(74.7/100*self.largeur, 15.48/100*self.hauteur, window=self.frame_joueurs, anchor=tk.NW)
		self.create_players_frame(4)

		self.frame_score = tk.LabelFrame(self.fenetre, text="SCORE", width=6.5/100*self.largeur, height=40/100*self.hauteur, bg="green")
		self.frame_score.pack()
		self.window_score = self.canvas.create_window(810.5,264,window=self.frame_score, anchor=tk.NW)
		self.change_resolution(self.largeur, self.hauteur)







	def add_player(self, info):
		info = ast.literal_eval(info)
		ide = int(info["ide"])
		self.other_player[ide] = info
		self.other_player[ide]["frame_nb"] = self.player_frame_count
		self.frame_joueurs_liste[self.player_frame_count]["nom"].config(text=info["name"])
		self.frame_joueurs_liste[self.player_frame_count]["nom"].pack()
		self.frame_joueurs_liste[self.player_frame_count]["score"].config(text=info["score"])
		self.frame_joueurs_liste[self.player_frame_count]["score"].pack()
		self.player_frame_count += 1
		print(self.other_player)
		client.printe("[+]PLAYER " + str(info["name"]) + " (" + str(ide) + ")", inpute=True)


	def scoring(self, ide, nb):
		if int(ide) == int(client.ide):
			self.score += int(nb)
			client.printe("you" + " scored " + str(nb) + " points", inpute=True)
		else:
			self.other_player[int(ide)]["score"] += int(nb)
			self.frame_joueurs_liste[self.other_player[int(ide)]["frame_nb"]]["score"].config(text=str(self.other_player[int(ide)]["score"])) #marche pas pck ide != ide
			client.printe("player " + str(self.other_player[int(ide)]["name"]) + " (" + str(ide) + ") scored " + str(nb) + " points", inpute=True)
		print(self.other_player)
		client.printe("player " + str(self.other_player[int(ide)]["name"]) + " (" + str(ide) + ") score " + str(nb) + " points", inpute=True)


	def deco(self, ide):
		print(self.other_player)
		for a in self.other_player.keys():
			print(self.other_player[a])
			if int(self.other_player[a]["ide"]) == int(ide):
				client.printe("[-]PLAYER " + str(self.other_player[a]["name"]) + " (" + str(ide) + ")", inpute=True)
				del self.other_player[a]
				break
		print(self.other_player)


	def create_players_frame(self, nb):
		self.player_frame_count = 0
		for a in range(0, nb):
			print("//////////")
			self.frame_joueurs_liste.append({})
			self.frame_joueurs_liste[a]["frame"] = tk.LabelFrame(self.frame_joueurs)
			self.frame_joueurs_liste[a]["frame"].grid(row=a//2, column=a%2, sticky="NESW")
			self.frame_joueurs_liste[a]["nom"] = tk.Label(self.frame_joueurs_liste[a]["frame"])
			self.frame_joueurs_liste[a]["nom"].pack()
			self.frame_joueurs_liste[a]["nom"].pack_forget()
			self.frame_joueurs_liste[a]["score"] = tk.Label(self.frame_joueurs_liste[a]["frame"])
			self.frame_joueurs_liste[a]["score"].pack()
			self.frame_joueurs_liste[a]["score"].pack_forget()
		#Penser a gerer les cas de + ou - de joueur


	def change_resolution(self, largeur, hauteur, nat=False):
		if nat == True:
			self.menu_size_nat = True
		else:
			self.menu_size_nat = False

		self.menu_size_size.set(largeur)
		self.hauteur = int(hauteur)
		self.largeur = int(largeur)
		self.fenetre.geometry(str(self.largeur)+"x"+str(self.hauteur))
		self.canvas.config(height=self.hauteur, width=self.largeur)
		global img
		img = Image.open("data/image/nsi_computer.PNG")
		img = img.resize((self.largeur,self.hauteur), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
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

		print(nat)
		print(self.menu_size_nat)
		print(self.largeur)
		print("//////////////////")
		#self.canvas.config(height=self.hauteur, width=self.largeur)


	def fullscreen(self):
		self.fullscreen_state = not self.fullscreen_state
		self.fenetre.attributes('-fullscreen', self.fullscreen_state)
		self.change_resolution(str(self.fenetre.winfo_screenwidth()), str(self.fenetre.winfo_screenheight()), nat=True)





	def epreuve1(self):
		self.epreuve_en_cour = 1
		self.ep1_phrase = "zfjezfkjzehfkjzehfkjezhfkzjhefzzekjfhezkjfz"
		self.ep1_label = tk.Label(self.frame_epreuve, text="RIEN")
		self.ep1_label.pack()
		self.ep1_entry = tk.Entry(self.frame_epreuve)
		self.ep1_entry.pack()
		self.ep_nbround = 0


	def ep1_Nround(self, ep1_phrase):
		print("hm")
		self.ep_time_begin = time.time()
		self.ep_nbround += 1
		self.ep1_phrase = ep1_phrase
		self.ep1_label.config(text=ep1_phrase)



	def epreuve2(self, ep2_choix1, ep2_choix2):
		self.epreuve_en_cour = 2
		self.ep2_reponse = "zfjezfkjzehfkjzehfkjezhfkzjhefzzekjfhezkjfz"
		self.ep2_label = tk.Label(self.frame_epreuve, text="waiting for serv")
		self.ep2_label.pack()
		bouton1 = tk.Button(self.frame_epreuve, text=ep2_choix1, command=lambda:[self.actualize(None, voulu=True, bouton=1)])
		bouton1.pack()
		bouton2 = tk.Button(self.frame_epreuve, text='les deux', command=lambda:[self.actualize(None, voulu=True, bouton=2)])
		bouton2.pack()
		bouton3 = tk.Button(self.frame_epreuve, text=ep2_choix2, command=lambda:[self.actualize(None, voulu=True, bouton=3)])
		bouton3.pack()
		self.ep_nbround = 0


	def ep2_Nround(self, ep2_question, ep2_reponse):
		self.ep_time_begin = time.time()
		self.ep2_label.config(text=ep2_question)
		self.ep2_reponse = ep2_reponse
		self.ep_nbround += 1



	def fin_round(self, winner):
		label_popup = tk.Label(self.frame_epreuve, text=str(winner)+"win round " +str(self.ep_nbround), font=("Bodoni MT", 30))
		label_popup.place(relx=0.5, rely=0.3, anchor="center")
        






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
		self.frame_console = tk.LabelFrame(fenetre, text="hisotrique", bg="black")
		self.frame_console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		#
		self.frame_console.update()
		self.console_log = tk.Label(self.frame_console, text="Bienvenue dans la console : \n", bg="red")
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
		client.printe(msg, output=True)
		a = msg.split(" ")
		if a[0] == "serv":
			client.send(str(" ".join(msg.split(" ")[1:])))
		elif a[0] == "connect":
			client.connect(str(" ".join(msg.split(" ")[1:-1])), a[-1])
		elif a[0] == "co":
			client.connect("{'name':'sacha'}", "localhost")
		elif a[0] == "con":
			client.connect("{'name':'test'}", "localhost")
		else:
			if a[0] == "resize":
				self.change_resolution(a[1], a[2])
			elif a[0] == "exit_console":
				pass
			elif a[0] == "info":
				client.printe("Info : \n"+str(self.other_player)+"\nIDE: \n"+str(client.ide)+"\nMy score :\n"+str(self.score))
			else:
				client.printe("Unknow command : " + str(a), output=True)
		self.console_entree.delete(0, tk.END)
		self.console_historique.append(msg)
		self.console_historique_nb = 0


	def console_fleche(self, event):
		self.console_entree.delete(0, tk.END)
		if str(event.keysym) == "Up":
			self.console_historique_nb += -1
		elif str(event.keysym) == "Down":
			self.console_historique_nb += 1
		if abs(self.console_historique_nb) > len(self.console_historique) or self.console_historique_nb < 0:
			if str(event.keysym) == "Up":
				self.console_historique_nb += 1
			elif str(event.keysym) == "Down":
				self.console_historique_nb += -1
		else:
			try:
				print(self.console_historique)
				print(self.console_historique_nb)
				self.console_entree.insert(0, self.console_historique[self.console_historique_nb])
			except:
				pass




	def actualize(self, KeyRelease, voulu=False, bouton=None):
		if self.epreuve_en_cour == 1:
			if tools.verif_text(self.ep1_phrase, self.ep1_entry.get()) == True:
				#EPREUVE 1 REUSSI
				temps = time.time() - self.ep_time_begin
				client.send("round_finish§" + str(temps))
		if self.epreuve_en_cour == 2:
			if voulu == True: 
				if bouton == int(self.ep2_reponse):
					print("gg")
					temps = time.time() - self.ep_time_begin
					client.send("round_finish§" + str(temps))
				else :
					print("tu es une merde")







client = Client()
Game()


#{"name": "sacha", "autre": 10}

"""
THEMATIQUE EPREUVE
BUG CHANGEMENT ROUND / EPREUVE (TEMPS ATTENTE, AFFIHAGE DE QUI GAGNE, ETC...)
BUG INERFACE JOUEUR
MENU DEMARER + INTRO

1/5

ptit bug menu a régler (mineur)*

PUBLIC!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




952-1049 = 97 (1366)
284-356 = 72  (768)
rapport : 100 largeure --> 74 hauteur
"""

