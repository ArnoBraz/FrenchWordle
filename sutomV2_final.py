# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:00:27 2025

@author: arnob
"""
import random
import customtkinter as ctk
import csv

## Parametre

def importe_csv(nom_fichier):
    with open(nom_fichier, 'r', encoding="utf-8", newline='') as fichier:
        lecteur = csv.DictReader(fichier,  delimiter=',')
        return [dict(ligne) for ligne in lecteur]

# alternative sans lexique
# mots = ["chat", "manger", "chien", "voir", "maison", "chanter", "arbre", "écrire", 
#     "voiture", "danser", "fleur", "lire", "ami", "parler", "école", "nager", 
#     "ordinateur", "cuisiner", "porte", "écouter", "table", "regarder", "livre", 
#     "courir", "fenêtre", "chanter", "vêtement", "écrire", "téléphone", "faire", 
#     "paysage", "respirer", "rue", "boire", "soleil", "apprendre", "étoile", 
#     "voyager", "montagne", "penser", "plage", "partir", "ciel", "agir", "chanson", 
#     "dormir", "ville", "étudier", "forêt", "regarder", "enfant", "apprécier", 
#     "restaurant", "demander", "lune", "écouter", "couleur", "planter", "musique", 
#     "réfléchir", "photo", "sauter", "bâtiment", "travailler", "saison", "sourire", 
#     "valise", "jouer", "porte-feuille", "rire", "semaine", "monter", "mois", 
#     "marcher", "année", "peindre", "pluie", "cuisiner", "vent", "répondre", "nuage", 
#     "jeter", "éclair", "remarquer", "étoile", "sentir", "nuage", "changer", "vague", 
#     "voler", "paysage", "voir", "saison", "toucher", "champ", "faire", "animal", 
#     "écrire", "homme", "parler", "femme", "raconter", "environnement", "courir", 
#     "document", "vendre", "ombre", "marcher", "forme", "arrêter", "gâteau", "réfléchir", 
#     "fête", "espérer", "voix", "recevoir"]

mots = importe_csv('lexique_sa.csv')
mots = list(map(lambda x: x['0'], mots))

#TODO : (+ input "entrée" pour soumettre)
## Génération 

def generation():
    global mots
    #mot = random.choice(tuple(lexique))
    mot = random.choice(mots)
    print(mot)
    return mot

def majuscule(mot_généré):
    transition = ''
    accents = { 'à': 'A', 'À': 'A', 'é': 'E', 'É': 'E', 'è': 'E', 'È': 'E', 'ê': 'E', 'Ê': 'E', 'ç': 'C', 'Ç': 'C', 'ù': 'U', 'Ù': 'U'}
    for elt in mot_généré:
        if not 65<=ord(elt)<=90 and 97<=ord(elt)<=122:
            transition+=chr(ord(elt)-32)
        elif elt in accents.keys():
            transition += accents[elt]
        elif 65<=ord(elt)<=90:
            transition += elt
        else: 
            transition += ' '
    return transition

# Création de la fenêtre (Custom)Tkinter :

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry("900x600")

titre = ctk.CTkFrame(master=root)
titre.pack(pady=1, padx=1, fill="both", expand=False)

label = ctk.CTkLabel(master=titre, text="Jeu du SUTOM !", text_color=["black", "white"], font=('Impact', 24))
label.pack(anchor="center")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


# Fonction de gestion des événements pour la saisie des lettres
def evenement(event, entry_list, indice):
    if event.keysym == "BackSpace":     #keysym dernier input réalisé
        if indice > 0 and not entry_list[indice].get():   #entry_list est la liste ayant les lettres de chaques cases
            entry_list[indice-1].focus_set()
            entry_list[indice-1].delete(0, ctk.END)
        
    if len(event.char) == 1: #Si + grande que 1 -> on change de case
        entry_list[indice].delete(0, ctk.END)
        entry_list[indice].insert(0, majuscule(event.char))
        if indice < len(entry_list) - 1:
            entry_list[indice+1].focus_set()


# Liste globale pour stocker toutes les lignes d'entrées
entry_hist = []  
trouvees = dict()
valide = True

def proposition(n, rep, k=0):
    global entry_hist  #Appel de la variable créer hors de la fonction
    global trouvees #Appel de la variable créer hors de la fonction
    global valide
    entry_list = []
    
    # Pour le place_holder
    if len(entry_hist)>0 and valide:
        for i, entry in enumerate(entry_hist[-1]):
            if majuscule(rep[i])==entry.get():
                trouvees[i] = entry.get()
            
    # Condition d'arrêt
    if len(entry_hist) == 0:
        gg = False
    else:
        gg = gagne(entry_hist, rep)
    
    # Création des cases
    if not gg:
        #Créer une nouvelle ligne d'entrées
        for i in range(1, n+1):
            if (len(entry_hist) > 0 and i-1 in trouvees.keys()) or i-1==0: 
                entry = ctk.CTkEntry(frame, width=40, font=('Roboto', 24), justify='center', fg_color="black", text_color="white", placeholder_text=majuscule(rep[i-1]), placeholder_text_color="green")
            else:
                entry = ctk.CTkEntry(frame, width=40, font=('Roboto', 24), justify='center', fg_color="black", text_color="white", placeholder_text="")
            entry.grid(row=k+2, column=i, padx=5, pady=20)
            entry.bind("<KeyRelease>", lambda event, idx=i-1: [evenement(event, entry_list, idx), anti_erreurs(entry_list, button1, rep)])
            entry_list.append(entry)
        len_mot = ctk.CTkLabel(master=frame, text=str(len(rep)), text_color=["black", "white"])
        len_mot.grid(row=k+2, column=i+1, pady=12, padx=10)
    
        # Stocke la liste d'entrées dans l'historique'
        entry_hist.append(entry_list)
        if len(entry_hist)!=1:
            entry_list[0].focus_set()
    
        # Bouton Soumettre avec mise à jour des couleurs des lignes précédentes
        button1 = ctk.CTkButton(frame, text="Soumettre", state='disabled', 
                                command=lambda: [update_colors(entry_hist, rep), proposition(n, rep, k+2), button1.configure(state="disabled")])
        button1.grid(row=k+2, column=0, pady=12, padx=10)
        
    # Si c'est gagné alors ..
    else:
        bravo = ctk.CTkLabel(master=frame, text=f"Bravo vous avez réussi en {(k//2)} coup(s) !", text_color=["black", "white"], font=('Impact', 24))
        bravo.grid(row=k+2, column=0, pady=12, padx=10)
        resetframe = ctk.CTkButton(frame, text="RECOMMENCER", command = frame_reset)
        resetframe.grid(row=k+4, column=0, pady=12, padx=10)

def anti_erreurs(entry_list, button1,  rep):
    condition = True
    for entry in entry_list:
        if entry.get() in (' ', ''):
            condition = False
    if condition:
        button1.configure(state="normal")  # Active le bouton
    else:
        button1.configure(state="disabled")  # Désactive le bouton

def update_colors(entry_hist, rep):
    global valide
    valide = True
    rep_maj = majuscule(rep)
    cpt_rep = dict()
    for lettre in rep_maj:
        if lettre not in cpt_rep.keys():
            cpt_rep[lettre] = 1
        else:
            cpt_rep[lettre] += 1

    prop = "".join(entry.get() for entry in entry_hist[-1]) # Conversion sous forme str entry_list (list())
    
    # Vérifier si le mot existe dans la liste "mots"
    if prop.lower() not in mots: # Met en minuscule la prop
        for entry in entry_hist[-1]:
            entry.configure(fg_color="red")  # Mettre en rouge si le mot n'existe pas
        valide = False

    else:
        for i, entry in enumerate(entry_hist[-1]):
            if entry.get() != rep_maj[i] and entry.get() in rep_maj and cpt_rep[entry.get()] > 0:
                entry.configure(fg_color="orange")
                cpt_rep[entry.get()] -= 1
            if entry.get() == rep_maj[i]:
                entry.configure(fg_color="green")
                cpt_rep[entry.get()] -= 1
    print()

 # Fonction vérification Gagne ?
def gagne(entry_hist, rep):
    prop = str()
    rep_maj = majuscule(rep)
    for entry in entry_hist[-1]:
        prop += entry.get()
    return prop == rep_maj

# Bouton de démarrage:
def demarrage():
    rep = generation()
    
    button1 = ctk.CTkButton(titre, text="Jouer", command = lambda: [proposition(len(rep), rep), button1.configure(state="disabled")])
    #button1.grid(row=1, column=0, pady=12, padx=10)
    button1.pack(anchor="center")

# Bouton de reset:
def frame_reset():
    global entry_hist, trouvees
    for widget in frame.winfo_children():
        widget.destroy()  # Supprime tous les widgets à l'intérieur du frame
    entry_hist, trouvees = list(),  dict() 
    titre.winfo_children()[1].destroy()
    demarrage()  

    
# Dark/Light mode
def color_mod():
    if switch.get() == "on" :
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')

color_frame = ctk.CTkFrame(master=root)
color_frame.pack(pady=1, padx=1, fill="both", expand=False)
switch = ctk.CTkSwitch(color_frame, text="Light Mode", command=color_mod, onvalue="off", offvalue="on")
switch.pack(pady=1, padx=1)

# Lancement de la boucle principale
demarrage()
root.mainloop()
