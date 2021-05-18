# coding: utf-8
import random


def verif_text(texte1, texte2):
	if str(texte1.lower()) == str(texte2.lower()):
		return True
	else:
		return False

def ep1_choix_phrase():
	liste = []
	f = open("data/ep1/phrases.txt", "r")
	for a in f :
		liste.append(a[:-1])
	return random.choice(liste)

def ep2_choix_question(theme):
	liste = []
	f = open("data/ep2/question.txt", "r")
	f = f.read().split("|")
	f = f[int(theme[2])]
	f = "".join(f).split("\n")
	for a in f[2:]:
		liste.append(a)
	liste = random.choice(liste[:-1])
	liste = ''.join(liste).split(';')
	return "§".join(liste)


def ep2_choix_theme():
	f = open("data/ep2/question.txt", "r")
	f = f.read().split("|")
	f = random.choice(f)
	f = "".join(f).split("\n")
	return f[1].split(";")




def test():
	for a in range(0, 10):
		print(ep2_choix_question(['Un clone', 'Un clown', '1']))

#print(ep2_choix_question(ep2_choix_theme()))
#print(ep2_choix_question(ep2_choix_theme()))

