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
    ennemi["vie"] = 5
    ennemi["force"] = d3 
    ennemi["degats"] = d3


def supprimer_ennemi():
    ennemi["nom"] = ""
    ennemi["vie"] = 0
    ennemi["force"] = 0
    ennemi["degats"] = 0

def creer_heros():
    heros["nom"] = "Arthur"
    heros["vie"] = 10
    heros["force"] = d3
    heros["energie"] = 10
    heros["degats"] = d3

def supprimer_heros():
    heros["nom"] = ""
    heros["vie"] = 0
    heros["force"] = 0
    heros["energie"] = 0
    heros["degats"] = 0
          
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

def test_sacrifice():
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
 

def combat(boost): 

    if int(boost) <= heros["energie"]:

        force_reelle = int(random.choice(heros["force"]))
        attaque = force_reelle + boost
        print "\nFORCE :", force_reelle, "+ SACRIFICE :", boost,
        print "\n= ATTAQUE :", attaque
        
        # on créé la force de l'ennemi
        force_ennemi_reelle = int(random.choice(ennemi["force"]))        
        print "%s déploie une FORCE de %s !" % (ennemi["nom"], force_ennemi_reelle)
        # on enlève l'énergie sacrifiée à l'énergie du héros
        heros["energie"] -= boost
             
        if attaque >= force_ennemi_reelle:
            degats_reel = int(random.choice(heros["degats"]))
            print "\nTu infliges %s de dégats à %s" % (degats_reel, ennemi["nom"])
            ennemi["vie"] -= degats_reel
            victoire()
            continuer()
            print caracs_heros()
            print caracs_ennemi()
            # print "La vie de %s est maintenant de %s" % (ennemi["nom"], ennemi["vie"])
            test_sacrifice()
        else:
            degats_ennemi_reel = int(random.choice(ennemi["degats"]))
            print "\n%s t'infliges %s de dégats! Aïe !" % (ennemi["nom"], degats_ennemi_reel)
            heros["vie"] -= degats_ennemi_reel
            gameover()
            continuer()
            print caracs_heros()
            print caracs_ennemi()
            test_sacrifice()
         
    else:
        print """
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!                                    !
! Pas assez d'énergie ! Recommence ! !
!                                    !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                
                """
        caracs_heros()
        caracs_ennemi()
        test_sacrifice()


# victoire et game over :    
def victoire():
    if ennemi["vie"] <= 0:
        print "!!!!!!!!!\nTu as éclaté %s !!!!!!!!!" % ennemi["nom"]
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
    supprimer_heros()
    creer_heros()
    start()
    continuer()
    rencontre()
    continuer()
    caracs_heros()
    caracs_ennemi()
    test_sacrifice()

ennemi = {}
heros = {}
    
jeu()
