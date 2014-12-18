 # -*- coding: utf-8 -*-
    
import sys
import random


def start():
    print """
***************
*             *
** SACRIFICE **
*             *
***************
    
Un jeu expérimental
de Damien Casoni (fieuuuh !)
    \n
    """
 
def continuer():
    raw_input("\nAppuie ENTREE pour continuer")

    	
def creer_ennemi():
    ennemi["nom"] = "Goblin"
    ennemi["vie"] = 10
    ennemi["force"] = d3 
    ennemi["degats"] = d3


def supprimer_ennemi():
    ennemi["nom"] = ""
    ennemi["vie"] = 0
    ennemi["force"] = 0
    ennemi["degats"] = 0

          
def rencontre():
    """
    Créé un ennemi et ses caracs
    """
    creer_ennemi()
    print "\nAttention %s ! Un %s se jette sur toi !" % (heros["nom"], ennemi["nom"])
    

def caracs_heros():
    """
    Affiche les caracs du héros
    """
    print "\n"
    print "%s :" % heros["nom"]
    print "VIE :", heros["vie"],
    print "|  FORCE : de", min(heros["force"]), "à", max(heros["force"]),
    print "|  DEGATS : de", min(heros["degats"]), "à", max(heros["degats"]),
    print "|  ENERGIE :", heros["energie"]
  
     
def caracs_ennemi():
    print "\n%s : " % ennemi["nom"]
    print "VIE :", ennemi["vie"],
    print "|  FORCE : de", min(ennemi["force"]), "à", max(ennemi["force"]),
    print "|  DEGATS : de", min(ennemi["degats"]), "à", max(ennemi["degats"])


# jeter les dés
d3 = range(1, 4)

def d(x):
    dx = range.d[1:x]
    resultat = int(random.choice(dx))
    dx = []


def sacrifice():
    """ 
    User peut sacrifier de l'énergie, il faut vérifier
    que ce soit bien en int

    """ 
    sacrifice = raw_input("\nCombien de points d'ENERGIE vas-tu sacrifier pour booster ton attaque ? ")
     
    try: 
        sacrifice = int(sacrifice)
        combat(sacrifice)        
         
    except ValueError:
		sys.exit("Interrution User")
        # print "Indique en chiffre combien de points d'ENERGIE tu veux sacrifier, tu peux mettre 0 si tu veux."
        # sacrifice ()
 

def combat(sacrifice): 

    if int(sacrifice) <= heros["energie"]:
        print "\n  FORCE : ", heros["force"], "\n+ SACRIFICE : ", sacrifice,
        attaque = int(random.choice(heros["force"])) + sacrifice
        print "\n= ATTAQUE : ", attaque
        # on enlève l'énergie sacrifiée à l'énergie du héros
        heros["energie"] -= sacrifice
             
        if attaque >= ennemi["force"]:
            print "\nTu infliges %s de dégats à %s" % (heros["degats"], ennemi["nom"])
            ennemi["vie"] -= heros["degats"]
            victoire()
            continuer()
            print caracs_heros()
            print caracs_ennemi()
            # print "La vie de %s est maintenant de %s" % (ennemi["nom"], ennemi["vie"])
            sacrifice()    
        else:
            print "\n%s t'infliges %s de dégats! Aïe !" % (ennemi["nom"], ennemi["degats"])
            heros["vie"] -= ennemi["degats"]
            gameover()
            continuer()
            print caracs_heros()
            print caracs_ennemi()
            sacrifice()
         
    else:
        print "\nPas assez d'énergie ! Recommence !"
        sacrifice()        


# victoire et game over :    
def victoire():
    if ennemi["vie"] <= 0:
        print "Tu as éclaté %s !!!" % ennemi["nom"]
        rencontre()
    else:
        None 
    
def gameover():
    if heros["vie"] > 0:
        print "Mais tu es toujours vivant."
    else:
        print """
        
+++++++++++++++++++++++++++++++
+                             +
+  Tu es mort... GAME OVER !  +
+                             +
+++++++++++++++++++++++++++++++
        """
        jeu()   


# le jeu commence ici

def jeu():
    start()
    continuer()
    rencontre()
    continuer()
    caracs_heros()
    caracs_ennemi()
    sacrifice()

heros = {
    "nom" : "Arthur",
    "vie" : 10,
    "force" : d3,
    "energie" : 10,
    "degats" : d3,
    }

ennemi = {}
    
jeu()        

        
