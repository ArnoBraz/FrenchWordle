import customtkinter as ctk
import subprocess


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Menu des Jeux")

app.geometry("790x600")
app.minsize(600, 400)

#fais en sorte qu'a l'appuie du bouton demarre le jeux
def lancer_quizz():
    subprocess.run(["python", "quizz.py"])
def lancer_Motus():
    subprocess.run(["python", "sutomV2_final.py"])

Titre = ctk.CTkLabel(app, text="Menu des Jeux", font=("Impact", 60))
Pres = ctk.CTkLabel(app, text="Vous pouvez selectionner l'un des jeux suivant :", font=("Impact", 30))
Titre.pack(pady=50)
Pres.pack(pady = 5)


#lancer le Motus
btn_motus = ctk.CTkButton(app, text="Motus", command=lancer_Motus,font=("Impact", 50),fg_color="#ff3333",hover=False)
btn_motus.pack(pady=30,padx = 20)
#lancer le quizz
btn_quizz = ctk.CTkButton(app, text="Quizz de culture aléatoire", command=lancer_quizz,font=("Impact", 50),fg_color="#ff3333",hover=False)
btn_quizz.pack(pady=15,padx = 0)


app.mainloop()