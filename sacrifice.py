 # -*- coding: utf-8 -*-
 
"""
Spend one week on creating the most interesting interactive fiction game possible.
Use:
 * lists
 * functions
 * modules (check ex13.py)
 * as many of new pieces of Python you can
  
Draw a map of your game on paper. Create the rooms, monsters, traps, etc.
 
The best way to work on a software:
 
1. Write a to-do list for your program.
2. Pick the easiest thing from your list.
3. Write English comments as guide for how you would accomplish this task
4. Write some code under the comments
5. Run your script to see if that piece of code works
6. Write new code > Run it > Fix it > Repeat
7. Cross the task in the to-do list, pick the next easiest task & repeat
 
======================
 
MY TO DO LIST :
 
======================
 
Un système de combat
VIE :
FORCE :
ENERGIE :
DEGATS :
 
Points d'énergie à sacrifier :
 
FORCE (x) + ENERGIE SACRIFIEE (y) = z
 
Si z >= force_ennemi
    alors - DEGATS à VIE ennemi
else:
    - DEGATS ennemi à VIE héros
     
Si vie hero = <= 0
    mort
 
Ennemis "statiques" (points fixes) pour commencer
 
"""
 
"""
A REIMPLEMENTER :
 
heros["nom"] = raw_input("Bienvenue vaillant héros ! Quel est ton nom ? ")
print "%s ?! Vraiment ?! Nous avons beaucoup entendu parler de toi !\n" % heros["nom"]
 
 
# Créer le game over   
if ["vie"] in heros["vie"] <= 0:
    print "GAME OVER"
else:
    print "OK"
 
     
print
Lorsque tu combats, tu peux sacrifier tes points d'ENERGIE afin de les ajouter à ton score de FORCE.
Si ce total ENERGIE + FORCE est supérieur à la FORCE de ton ennemi tu infliges des DEGATS à celui-ci.
Si ce total est inférieur à la FORCE de ton ennemi, c'est lui qui t'infliges des dégats.
Si ta VIE descend à 0, tu meurs et ton aventure prends fin.
\n
"""
 
 
def continuer():
    raw_input("Appuie ENTREE pour continuer")
 
     
def caracs_heros():
    """
    Affiche les caracs du héros
    """
    print "\n"
    print "Voici tes caractéristiques %s :" % heros["nom"]
    print "VIE : ", heros["vie"]
    print "FORCE : ", heros["force"]
    print "ENERGIE : ", heros["energie"]
    print "DEGATS : ", heros["degats"]
    print "\n"
  
  
def rencontre():
    """
    Affiche un ennemi et ses caracs
    """
    print "Attention %s ! Un %s se jette sur toi !" % (heros["nom"], ennemi["nom"])
     
def caracs_ennemi():
    print "\nVoici les caractéristiques de %s : " % ennemi["nom"]
    print "VIE : ", ennemi["vie"]
    print "FORCE : ", ennemi["force"],"\n"
 
 
def combat():
 
    sacrifice = raw_input("\nCombien de points d'ENERGIE vas-tu sacrifier pour booster ton attaque ? ")
     
    try:
     
        sacrifice = int(sacrifice)
         
        if int(sacrifice) <= heros["energie"]:
            print "\n  FORCE : ", heros["force"], "\n+ ENERGIE : ", heros["energie"], "\n+ SACRIFICE : ", sacrifice,
            attaque = heros["force"] + heros["energie"] + sacrifice
            print "\n= ATTAQUE : ", attaque
            # on enlève l'énergie sacrifiée à l'énergie du héros
            heros["energie"] -= sacrifice
             
            if attaque >= ennemi["force"]:
                print "\nTu infliges %s de dégats à %s" % (heros["degats"], ennemi["nom"])
                ennemi["vie"] -= heros["degats"]
                print caracs_ennemi()
                # print "La vie de %s est maintenant de %s" % (ennemi["nom"], ennemi["vie"])
        
            else:
                print "\n%s t'infliges %s de dégats! Aïe !" % (ennemi["nom"], ennemi["degats"])
         
        else:
            print "\nPas assez d'énergie ! Recommence !"
            combat()
    
         
             
         
    except ValueError:
     
        print "Indique en chiffre combien de points d'ENERGIE tu veux sacrifier, tu peux mettre 0 si tu veux."
        combat()
 
  
heros = {
    "nom" : "Arthur",
    "vie" : 10,
    "force" : 5,
    "energie" : 10,
    "degats" : 2,
    }
 
ennemi = {
    "nom" : "Goblin",
    "vie" : 10,
    "force" : 20,
    "degats" : 5,
    }
 
 
rencontre()
 
continuer()
 
caracs_heros()
 
caracs_ennemi()
 
continuer()
 
combat()
