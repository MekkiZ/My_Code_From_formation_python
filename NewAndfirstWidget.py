#coding :utf-8

import tkinter


'''le widget c'ets le term quon emploi pour tout mettre dans un fentre, allez voir la playliste de tkinter

le principeest toujkours le mme :

nom de la variable = nom du widget (widget parent, paraetres ...)

'''

app= tkinter.Tk()

#lablel_walcome = tkinter.Label(app, text="miklar le rustre") #seul, python ne sauras pascomemnt l'afficher on va devoir le parametrer

#lablel_walcome.pack()# pack va separer linterface en dux , elle va reserver u espace pour elle, on peux posiiton par gri ou par pixel,

#on peux recuprer un paremetre et l'afficher sur le terminal grace a la methode cget(nom du parametre)
#Pour changer le text par ecemple dans un parametre on peut utilisrr la methode config() : exemple : label_welcom.config(text="salut toi")

#Pour avoir un text mais ceci non pas comme un label mais comme un message avec de retour a ligne auto, on feras : message_walcome = tkinter.message(app, text="miklar le rustre")

# pour mettre un widget decriture ( taille de 20 par default) on va utiliser la fonction Entry()

#entry_now= tkinter.Entry(app, width=45, show='*') 
#entry_now.pack()

#creation d'un widget button avec une function ; 
"""
def boucle():
    for i in range(20):
        print(i)
        i =+1
        
    

boutton_quit = tkinter.Button(app, text="OK", command=boucle)
boutton_quit.pack()
"""

#widget pour cocher la case dans les application python

check_widget = tkinter.Checkbutton(app, text="coche si tu est un humain" , offvalue=2, onvalue=5, height=34, width=50) # il y as des valeur pardefault si on veux changer cela on as une methode qui est offvakue()
radio_widget= tkinter.Radiobutton(app, text="homme", value=1)
radio_widget2= tkinter.Radiobutton(app, text="homme", value=1)



radio_widget2.pack()
radio_widget.pack()
check_widget.pack()















app.mainloop()