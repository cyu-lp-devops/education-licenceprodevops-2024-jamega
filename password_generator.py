from tkinter import Label, Button, Checkbutton, Tk, IntVar, Entry, StringVar, DISABLED, NORMAL
import tkinter.ttk as ttk
from random import choice, randint

alphabet_min = [ chr(i) for i in range(97,123) ]
alphabet_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

class Generateur:
    def __init__(self, window):
        self.window = window
        window.geometry('450x350')
        window.title('Générateur de mot de passe')
        window.resizable(1,0)

        Label(window, text = "Nombre de caractères :").place(x = 5 , y = 5)
        self.nombre_caracteres = IntVar(window,value=20)
        self.n = Entry(window, width=3, textvariable=self.nombre_caracteres)
        self.n.place(x = 140, y=6)

        Label(window, text = "Alphabets à prendre en compte :").place(x = 5 , y = 40)
        self.checkMin = IntVar(value=1)
        self.min = Checkbutton(window, text = 'Lettres minuscules :\n' + ', '.join(alphabet_min), variable = self.checkMin, width = 56)
        self.min.place(x=0,y=60)

        self.checkMaj = IntVar(value=1)
        self.maj = Checkbutton(window, text = 'Lettres majuscules :\n' + ', '.join(alphabet_maj), variable = self.checkMaj, width = 60)
        self.maj.place(x=0,y=100)

        self.checkChiffres = IntVar(value=1)
        self.chif = Checkbutton(window, text = 'Chiffres : ' + ', '.join(chiffres), variable = self.checkChiffres, width = 35)
        self.chif.place(x=0,y=140)

        self.checkCS = IntVar(value=1)
        self.cs = Checkbutton(window, text = 'Caractères spéciaux : ' + ', '.join(caracteres_speciaux), variable = self.checkCS, width = 51)
        self.cs.place(x=0,y=160)

        self.checkPerso = IntVar(value=0)
        self.liste_perso = StringVar()
        self.listePerso = Checkbutton(window, text = 'Caractères personnels :', variable = self.checkPerso, width = 18, command=self.toggle_perso)
        self.listePerso.place(x=0,y=200)
        self.perso = Entry(window, width=30, textvariable=self.liste_perso, state=DISABLED)
        self.perso.place(x = 160, y=205)
        Label(window,text='(à la suite,sans virgule)').place(x=25,y=230)

        gener = Button(window, text = 'Générer',  width = 15, font = ('Tahoma', 10), command = self.pwd)
        gener.place(x = 170 , y = 250)
        
        self.generated_pwd = StringVar()
        self.result_label = Label(self.window, textvariable=self.generated_pwd)
        self.result_label.place(x=5, y=280)

        self.copie_presse_papier = Button(self.window, text = 'Copier en mémoire',  width = 20, font = ('Tahoma', 10), command = self.memory)
        self.copie_presse_papier.place(x = 150 , y = 300)
        self.copie_presse_papier.config(state=DISABLED)

    def toggle_perso(self):
        if self.checkPerso.get() == 1:
            self.perso.config(state=NORMAL)
        else:
            self.perso.config(state=DISABLED)

    def pwd(self):
        n = int(self.n.get())
        min = int(self.checkMin.get())
        maj = int(self.checkMaj.get())
        chif = int(self.checkChiffres.get())
        cs = int(self.checkCS.get())
        perso = int(self.checkPerso.get())

        self.style = dict()
        i = 0
        
        if min == 1:
            self.style[i] = alphabet_min
            i += 1
        if maj == 1:
            self.style[i] = alphabet_maj
            i += 1
        if chif == 1:
            self.style[i] = chiffres
            i += 1
        if cs == 1:
            self.style[i] = caracteres_speciaux
            i += 1
        if perso == 1 and self.liste_perso.get().strip():
            self.style[i] = list(self.liste_perso.get().strip())
            i += 1

        if i == 0:
            self.generated_pwd.set("Veuillez sélectionner au moins un type de caractère.")
            self.copie_presse_papier.config(state=DISABLED)
            return

        self.pwd = ''.join(choice(self.style[randint(0,i-1)]) for _ in range(n))
        
        self.generated_pwd.set('Mot de passe généré : ' + self.pwd)
        self.copie_presse_papier.config(state=NORMAL)

    def memory(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.pwd)
        self.window.update()

root = Tk()
app = Generateur(root)
root.mainloop()
