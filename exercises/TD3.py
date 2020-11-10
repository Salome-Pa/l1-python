#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

#
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))  











def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
Créer une fonction d'affichage d'un temps afficheTemps. Attention, les mots jour, heure et seconde doivent être au pluriel s'il y en a plusieurs. S'il y en a zéro, ils ne doivent pas apparaître. print(message, end="") permet de ne pas sauter une ligne après un print. Vous pouvez écrire une fonction qui affiche un mot au pluriel ou non, appelée ensuite plusieurs fois par afficheTemps pour simplifier votre code.

In [ ]:
#fonction auxiliaire ici

def afficheTemps(temps):
    pass
    
afficheTemps((1,0,14,23))
Ecrire une fonction qui demande à l'utilisateur de rentrer un nombre de jours, d'heures, de minutes et de secondes et qui renvoie un temps. Attention, si l'entrée utilisateur n'est pas correcte, par exemple 80 minutes, afficher un message d'erreur et s'arrêter.

(Optionnel) Au lieu d'arêter le programme, demander de rentrer une nouvelle valeur, tant que ce n'est pas une valeur correcte.

def demandeTemps():
    jour = int(input("combien de jours"))
    heure = int(input("combien d heures"))
    minute = int(input("combien de minutes"))
    seconde = int(input("combien de sec"))
    if (seconde > 59 or minute > 59 or heure > 23):
        print("entree mal formee, ce n est pas une date")
        return (0,0,0,0)
    return (jour,heure,minute,seconde)
afficheTemps(demandeTemps())



'''In [ ]:
def demandeTemps():
    pass

afficheTemps(demandeTemps())
On veut être capable d'additionner deux temps. Donner une fonction qui fait ce calcul, en utilisant les fonctions précédentes.'''

def sommeTemps(temps1,temps2):
     return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))




In [ ]:
def sommeTemps(temps1,temps2):
    pass

sommeTemps((2,3,4,25),(5,22,57,1))
On veut maintenant calculer un pourcentage d'un temps. Par exemple, 20% de 2 jours et 36 minutes correspond à 9 heures, 43 minutes et 12 secondes.

def proportionTemps(temps,proportion):
    return secondeEnTemps(int(tempsEnSeconde(temps)*proportion))

    #tempsEnSeconde(temps)*proportion (0.2) --> nb sec (pas float mais int(nb seconde)
     afficheTemps(proportionTemps((2,0,36,0),0.2))
     afficheTemps(proportionTemps(proportion = 0.2, temps = (2,0,36,0)))
Implémenter la fonction proportionTemps puis appeler cette fonction en échangeant l'ordre des arguments mais en les nommant.



In [ ]:
def proportionTemps(temps,proportion):
    pass
afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments
On veut maintenant afficher un temps sous forme de date, en supposant que le temps 0 est le 1 janvier 1970 à 00:00:00.

Implémenter une fonction tempsEnDatequi donne la date sous la forme (année, jour, heure, minute, seconde).
Implémenter la fonction afficheDatequi affiche la date.
(Optionnel) Gérer également les mois.
In [ ]:
def tempsEnDate(temps):
    pass

def afficheDate(date = -1):
    pass
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()
Il existe des fonctions dans la librairie time pour la gestion du temps. En particulier, il existe une fonction time qui donne le temps écoulé depuis 1970 en secondes. La trouver avec la documentation python et la tester en utilisant afficheDate. Tester de la même manière la fonction time.gmtime qui réalise une tâche similaire à tempsEnDate. Que constatez vous ?

In [ ]:
#tester ici les fonctions de la librairie time
Attention, tous les 4 ans les années sont bisextiles (un jour de plus) sauf les multiples de 100 qui ne sont pas des multiples de 400. Donner un code qui prend un nombre de jours et affiche toutes les années bisextiles depuis 1 janvier 2020 à 00:00:00 jusqu'à la fin de ces jours.

In [ ]:
def bisextile(jour):
    pass
        
bisextile(20000)
Implémenter une fonction nombreBisextile qui calcule le nombre d'années bisextiles pour un nombre de jour donnés pour corriger votre fonction de calcul de la date.

In [ ]:
def nombreBisextile(jour):
    pass

def tempsEnDateBisextile(temps):
    pass
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
Ajouter des valeurs par défaut dans le code de afficheDate afin de pouvoir ommettre l'argument de ces fonctions. Dans ce cas là, on affichera la date actuelle en utilisant la fonction time.

On va maintenant inspecter notre code pour améliorer sa qualité:

Regarder tous les warnings donnés par flake8 et essayer de les régler.
Utiliser le debugger (F5) pour étudier le fonctionnement de votre fonction nombreBisextile.
Mettre les annotations de type des arguments et du retour de la fonction pour nombreBisextile et une autre fonction de votre choix. Vérifier avec mypy que tout fonctionne bien.
Donner une fonction qui vérifie la charge horaire d'un employé, donnée sous forme d'une liste de temps travaillé chaque semaine dans un mois. Il ne faut pas dépasser 48h par semaine et 140h par mois (qu'on considère ici de 4 semaines).

(Optionnel) S'adapter à une liste qui peut contenir plusieurs mois.

In [ ]:
def verifie(liste_temps):
    pass


liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)