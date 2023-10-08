from tkinter import *
import webbrowser

#création d'une fonction pour ouvrir un lien linkedin
def open_lkd_link():
    webbrowser.open_new("https://www.linkedin.com/in/mattis-beaugendre/")

#création d'une fenêtre
window = Tk()

#personnalisation de la fenêtre
window.title("Le wallet de Monsieur Beaugendre")
#remplacer le logo présent dans la barre supérieur de la fenêtre, il faut bien penser à convertir l'image au format ICO
window.iconbitmap("ressources\logo-iroxx.ico")
#changer la couleur du fond
window.config(background='#26B77F')

#redimension la fenêtre
window.geometry("1080x720")
window.minsize(480, 360)
window.maxsize(1280,1080)


#création d'une box pour positionner le texte comme on le souhaite
box = Frame(window, bg = "#26B77F", bd = YES, relief=SUNKEN)

#texte
label_title = Label(box, 
                    text="Bienvenue sur l'interface crypto de MattisBe",
                    font=("Banhspricht",20),
                    bg="#26B77F",
                    fg="white"
                    )
label_title.pack()

label_subtitle = Label(box, 
                    text="Bienvenue sur l'interface crypto de MattisBe",
                    font=("Banhspricht",12),
                    bg="#26B77F",
                    fg="white"
                    )
label_subtitle.pack()

#creation d'un bouton
lkd_button = Button(box, text="Retrouve-moi sur LinkedIn", bg="white", font=("Banhspricht",12), fg="#26B77F", command=open_lkd_link)
lkd_button.pack(padx=10, pady=25, fill=X)

box.pack(expand=YES)


#affichage de la fenêtre
window.mainloop()