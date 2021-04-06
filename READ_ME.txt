POUR LANCER LE PROGRAMME : 
(normalement toute les bibliothèques sont installé par défaut)

METHODE 1 (vous avez de la chance) : 
	ouvrez simplement launch.bat (cela lance le programme serv.py et main.py)
	(note : on peut aussi d'abord ouvrir serv.bat puis main.bat)

METHODE 2 (vous n'avez pas de chance) : 
	ouvrez anaconda prompt (ananconda en ligne de commande)
	allez dans ce répertoire
	tapez : python serv.py
	ouvrez un autre anaconda prompt
	allez dans ce répertoire
	tapez : python main.py



Ensuite deux fenetre s'ouvriront
Dans la fentre intitulé console : 
tappez : connect {"name": "test", "autre": 10} 
(note vous pouvez bien evidement changer la valeur de "name" (en un str) et de "autre")
vous pouvez maintenant tapez les commandes : 
	serv ping (vous répondra : pong)
	serv lancement (répondra lancement sur tous les main.py lancés)


Notre prochain objectif et de créer une première épreuve.