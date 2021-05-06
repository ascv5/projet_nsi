import random


def verif_text(texte1, texte2):
	if str(texte1.lower()) == str(texte2.lower()):
		return True
	else:
		return False

def choix_phrase():
	liste = []
	f = open("data/ep1/phrases.txt", "r")
	for a in f :
		liste.append(a[:-1])
	return random.choice(liste)

def ep2_choix_question():
	liste = []
	f = open("data/ep2/question.txt", "r")
	for a in f :
		liste.append(a[:-1])
	liste = random.choice(liste)
	liste = ''.join(liste).split(';')
	return "§".join(liste)

