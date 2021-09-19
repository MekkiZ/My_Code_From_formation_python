#coding:utf-8


import tkinter


"""
commentaire important sur le sujet :

oon peut cre une fenetre principal avec la methode constructuer

un widget est un fenetre, une interface, un bouton , tout est ajouter dans un ceci c'est un widget, qu'on cree exempl ace tkinter  : mainapp = tkinter.Tk()
                                                                        mainapp.mainloop()          







"""

mainapp = tkinter.Tk()
mainapp.title("mon premier programe")
#mainapp.geometry(XxY+10+10")#pour la dimension de la fenetre, un position de la fenetre  , elle peux prendre plusieur parametrer, x = la largeur e pixel x y= la hauteur en pixel ,
#pour centrer la fenetr eil faut determner la position en x et la position en y, pour 'x' sa positoon c'est la largeur de lecran diver par 2 et retirer la surface '-' la moitier de la largeur de la fenetrer divsier 2
#position_x= (largeur_ecran//2) - (largeur_fenetre//2)
##position_y= (hauteur_ecran//2) - (hauteur_fenetre//2)

'''

exemple : 

screen_x= int(mainapp.winfo_screenwidth()) : il va recuprer la resolution de lecran, pour quill recuprer sur lordi
screen_y=int(mainapp.winfo_screenwidth()) : il va recuprer la resolution de lecran, pour quill recuprer sur lordi
window_x= 800
window_y= 600
geo= f'{window_x}x{window_y}+{screen_x}+{screen_y}'
#position_x= (screen_x//2) - (window_x//2)
##position_y= (screen_y//2) - (window_y//2)

Trouver un mouyen pour centrer parfaitement avec une focntion 


'''
screen_x=int(mainapp.winfo_screenwidth()) #: il va recuprer la resolution de lecran, pour quill recuprer sur lordi
screen_y=int(mainapp.winfo_screenwidth()) #: il va recuprer la resolution de lecran, pour quill recuprer sur lordi
window_x= 800
window_y= 600

posX= (screen_x//2) - (window_x//2)
posY=  (screen_y//2) - (window_y//2)

geo= f'{window_x}x{window_y}+{posX}+{posY}'

mainapp.geometry(geo)


#mainapp.minsize('640x480') #dimension minimal
#mainapp.maxsize('1280x720')#dimension maximal
#mainapp.resizable(width=False, height=True)   #interdire leur dimensionement






mainapp.mainloop()
#mainapp.quit() #pour quiter la fenetre sans lacroix rouge




