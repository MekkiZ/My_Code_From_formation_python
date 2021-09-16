import pickle

'''
commentaire pour formation , tout les commentaire que je pense etre important je le note ici, 

les tuplesont immuable, on ne peux pas les mofidifier avce methode etc, onp uex cree mais apres il ne bouge pas.
conteneur sequence : tuples, la diference avce la liste c'est quiya sune sequence avec des objet

on peux affectuer plusiur ultiple dans les tuples expl : (exemple1, exemple2)= (Valeur_exp1, Valeur_exp2)
autre inventage , on va pouvoir fair eun retour multiple de fonctiona vec deux valeur exple :   

                def get_player_position():
                    posX= 148
                    posY = 86

                    return (psX, posY )  # ceci une des bonne chosed des tuples


'''



#liste : on utilise des crochet []

liste = ["mekki", "maman", "soeur", "frere", "pere", "oncle","tante","neuveu","niece"]

for Key_object, Value_object in enumerate(liste):
    print(f"{Key_object} --> {Value_object}")




#tuples: ici on utilise des () et rajouter ',' 


tuple1= (45,)



"""
informaton importante

fichier :

mode d'ouverture  : r (lecture seule)
                    w(ecriture avec remplacement)
                    a (ecriture avecajout en fin de difhcier)
                    x(lecture et ecrire)
                    r+ ( lecture/ecriture dzasn un meme fichier)

tout fichier ouvert doit etre fermer avec close()

les ' \n' serve pour des retour a la ligne

dump = sert pour le copi del'objet

rcezfze


"""
fic = open('fichier1.txt', 'r')

print(fic.read())
fic.close()


with open('fichier1.txt', 'r') as fic:
    print(fic.read())


if fic.closed:
    print("le fcihier est fermé")

    
    
class Players:
    def __init__(self, name, level) -> None:
        self.name=name
        self.level=level
    def whoami(self):
        print(f'{self.name} [{self.level}]')



with open('Joueur.data','rb') as fichier:
    get_record= pickle.Unpickler(fichier)
    player_one= get_record.load()


player_one.whoami()