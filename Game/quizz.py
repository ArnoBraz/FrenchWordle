import customtkinter as ctk
from tkinter import messagebox
import random



questions = [
    {"question": "Quelle est la capitale de la Malaisie?", "options": ["Sepang", "Mandalika", "Kuala Lumpur", "Jakarta"], "answer": "Kuala Lumpur"},
    {"question": "Quel est le plus grand océan du monde?", "options": ["Atlantique", "Pacifique", "Indien", "Arctique"], "answer": "Pacifique"},
    {"question": "Qui a peint la Joconde?", "options": ["Van Gogh", "Picasso", "Da Vinci", "Monet"], "answer": "Da Vinci"},
    {"question": "Combien de planètes y a-t-il dans le système solaire?", "options": ["7", "8", "9", "10"], "answer": "8"},
    {"question": "Quelle est la langue la plus parlée dans le monde?", "options": ["Anglais", "Mandarin", "Espagnol", "Hindi"], "answer": "Mandarin"},
    {"question": "Qui a écrit 'Les Misérables'?", "options": ["Victor Hugo", "Emile Zola", "Molière", "Voltaire"], "answer": "Victor Hugo"},
    {"question": "Quel est le plus grand pays du monde?", "options": ["États-Unis", "Canada", "Chine", "Russie"], "answer": "Russie"},
    {"question": "Quel est l'élément chimique dont le symbole est 'O'?", "options": ["Or", "Oxygène", "Ozone", "Osmium"], "answer": "Oxygène"},
    {"question": "Qui a découvert la gravité?", "options": ["Galilée", "Newton", "Einstein", "Darwin"], "answer": "Newton"},
    {"question": "Dans quel pays a été inventé le vélo?", "options": ["France", "Allemagne", "Angleterre", "Italie"], "answer": "Allemagne"},
    {"question": "Pourquoi ?", "options": ["Jsp!", "oui!", "C'est la mer noire'", "réponse d"], "answer": "réponse d"},
    {"question": "Quel est la companie la plus favorisé au monde fin 2024 ?", "options": ["Google", "Nvidia", "Microsoft", "Apple"], "answer": "Nvidia"},
    {"question": "A quel Grand Prix s'est décidé le championnat du monde de Formule 1 2021 ?", "options": ["Quatar", "Etats Unis", "Emirats Arabe Unis", "Arabie Saoudite"], "answer": "Emirats Arabe Unis"},
    {"question": "Quel est la masse d'une fourmi ?", "options": ["50 mg", "10 mg", "1 g", "100 mg"], "answer": "10 mg"},
    {"question": "Qui a gagné la coupe du monde de Rugby en 2024 ?", "options": ["France", "Nouvelle Zélande", "Afrique du sud", "Australie"], "answer": "Afrique du sud"},
    {"question": "Quels sont les 4 premières décimales de pi/2 ?", "options": ["5702", "5710", "5707", "5720"], "answer": "5707"},
    {"question": "Quel citation n'est pas tirée du film OSS-117 : Le Caire nid d'espion ?", "options": ["J'aime me beurrer la biscotte", "J'aime me battre", "J'aime danser la samba", "J'aime les panoramas"], "answer": "J'aime me beurrer la biscotte"},
    {"question": "Quel phénomène est à l'origine des aurores boréales ?", "options": ["La réfraction de la lumiere dans l'atmosphère", "l'interaction entre le vent solaire et la magnétosphère terrestre", "la combustion des gaz atmosphériques à haute altitude", "la réflexion de la lumiere solaire sur les pôles"], "answer": "l'interaction entre le vent solaire et la magnétosphère terrestre"},
    {"question": "Qui a inventé le language de programmation python ?", "options": ["Guido van Rossom", "Graham Bell", "Dennis Ritchie", "Jensen Huang"], "answer": "Guido van Rossom"},
    {"question": "Dans le jeu Dark souls 3, quel est le nom du boss secret de la zone optionelle : La cité enclavée ?", "options": ["Midir le mange-ténèbres", "Roi sans nom", "Soeur Friede", "Père Ariandel"], "answer": "Midir le mange-ténèbres"},
    {"question": "Sur la boite de jeu monster hunter 4 ultimate, quelle arme porte le personnage sur la photo ?", "options": ["Une volto-hache", "Un insectoglaive", "Un marteau", "Une grande épée"], "answer": "Une volto-hache"},
    {"question": "Dans le jeu Sekiro, Quel est le metier du personnage ?", "options": ["Faux Samourai", "Shinobi", "Chevalier", "Marchand"], "answer": "Shinobi"},
    {"question": "Quel est le piment qui a été considéré comme le plus piquant au monde le plus longtemps ?", "options": ["Red Savina", "Habanero", "Buth Jolokia", "Le carolinna reaper"], "answer": "Le carolinna reaper"},
    {"question": "Combien y avait-il de pays reconnu par l'ONU en 2024 ?", "options": ["227", "221", "193", "198"], "answer": "193"},
    {"question": "Combien de km/h pour un noeud (Pour un bateau) ?", "options": ["1.934", "1.852", "1.656", "1.704"], "answer": "1.852"},
    {"question": "Combien y a-t-il de portes à Thèbes dans la pièce les 7 contre Thèbes de Eschyle ?", "options": ["2", "7", "5", "9"], "answer": "7"},
    {"question": "Combien d'année a durée la 2e république ?", "options": ["2 ans", "4 ans", "20 ans", "40 ans"], "answer": "4 ans"},
    {"question": "Quelle est l'année de création de microsoft ?", "options": ["1980", "1947", "1975", "1989"], "answer": "1975"},
    {"question": "Intel est l'abrévation de quelle proposition ?", "options": ["Institute of Elements", "Institute of Electronics", "Intelligent Elements", "Integrates Electronics"], "answer": "Integrates Electronics"},
    {"question": "Quel est le nom scientifique du koala ?", "options": ["Monodon monoceros", "Folivora", "Euspinolia militaris", "Phascolarctos cinereus"], "answer": "Phascolarctos cinereus"},
    {"question": "Dans les Suppliantes, quelle est la fonction du représentant des fils d'Egyptos ?", "options": ["Messager", "Herault", "Toubib", "Bouffon"], "answer": "Herault"},
    {"question": "En quelle année a été créer le jeu Dofus ?", "options": ["2004", "2000", "2005", "2007"], "answer": "2004"},
    {"question": "Quel est le nom de l'espèce qui est le croisement d'un grizzli et d'un ours blanc ?", "options": ["Grolar", "Coquard", "ligre", "ours à moustache"], "answer": "Grolar"},
    {"question": "Comment s'apelle l'allergie des chats ?", "options": ["CGEF", "CEGF", "GCEF", "FEGC"], "answer": "CGEF"},
    {"question": "Quel est le prénom du joueur qui a récuperer le plus d'argent dans l'emission les douzes coups de midi ?", "options": ["Emilien", "Xavier", "Alexandre", "Corentin"], "answer": "Emilien"},
    {"question": "Quel est l'oiseau qui à la plus longue queue ?", "options": ["une pie", "une quiscale", "un mésange", "une orite"], "answer": "une quiscale"},
    {"question": "Ou se trouve la salle des SPE D ?", "options": ["Pascal", "Einstein", "Descartes", "Napoléon"], "answer": "Einstein"},
    {"question": "Comment s'appelle l'emission qui est animé sur twitch par le streamer Etoiles qui consiste à regarder l'emission question pour un champion ?", "options": ["La nuit de la culture", "Touche pas à mon poste", "Le jour du savoir", "Le react de minuit"], "answer": "La nuit de la culture"},
    {"question": "En musculation quel est la methode d'entrainement qui de gagner le plus efficacement de la masse musculaire", "options": ["La force", "L'hypertrophie", "l'altérophilie'", "L'endurance"], "answer": "L'hypertrophie"},
    {"question": "Quel est le nom de la marque du produit le plus utiliser par les bricoleurs pour proteger, nettoyer, dégripper...", "options": ["WD-40", "Trickshot", "Vaseline", "M-40"], "answer": "WD-40"}

]


def reset_quiz():
    global current_question, score, remaining_time

    # Réinitialisation
    current_question = 0
    score = 0
    remaining_time = 15

    # Annule le timer
    try:
        root.after_cancel(timer)
    except NameError:
        pass

    for widget in root.winfo_children():
        widget.destroy()

    return demarrage()

#programmation du timer
def update_timer():
    global remaining_time, timer
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.configure(text=f"Temps restant : {remaining_time} s")
        timer = root.after(1000, update_timer)
    else:
        afficher_q_c()
        root.after(1000,charger_prochaine_q)

#reponse fausse rouge / vraie vert
def check_answer(selected_option):
    global current_question, score
    root.after_cancel(timer)

    for btn, option in option_buttons.items():
        if option == selected_option:
            if option == questions[current_question]["answer"]:
                btn.configure(fg_color="green")
                score += 1
            else:
                btn.configure(fg_color="red")

    afficher_q_c()
    root.after(400, charger_prochaine_q)

#afficher en vert la question correct
def afficher_q_c():
    correct_answer = questions[current_question]["answer"]
    for btn, option in option_buttons.items():
        if option == correct_answer:
            btn.configure(fg_color="green")

#charger les prochaines questions et faire le scipt de fin
def charger_prochaine_q():
    global current_question, remaining_time
    current_question += 1
    if current_question < num_questions:
        remaining_time = 15
        reponse_a()
    else:
        messagebox.showinfo("Quiz terminé", f"Votre score est {score}/{num_questions}")
        if score == num_questions:
            messagebox.showinfo("SCORE", f"NICE !!! ")
        elif score == 0:
            messagebox.showinfo("SCORE", f"TU REFLECHIS OUUUU ?")
        reset_button = ctk.CTkButton(root, text="Réinitialiser", font=("Arial", 16), command=reset_quiz)
        reset_button.grid(row=4, column=1, columnspan=2, pady=10)

#placer aleatoirement les reponses et les réponses et le timer
def reponse_a():
    global timer
    question_label.configure(text=questions[current_question]["question"])
    question_label.grid(row=1, column=1, columnspan=2, pady=20, padx=10, sticky="nsew")

    options = questions[current_question]["options"]
    random.shuffle(options)

    for i, btn in enumerate(option_buttons):
        option_buttons[btn] = options[i]
        btn.configure(text=options[i], command=lambda opt=options[i]: check_answer(opt), fg_color="#7100cf", hover=False)

    timer_label.configure(text=f"Temps restant : {remaining_time} s",)
    timer = root.after(100, update_timer)

#initialiser le quizz et faire en sorte que tout marche bien (obliger d'utiliser du try/except pas trouver d'autre solution)
def start_quiz():
    global num_questions
    try:
        num_questions = int(num_questions.get())
        if num_questions <= 0 or num_questions > len(questions):
            raise ValueError("Réessayer!  Le nombre de questions doit être entre 1 et " + str(len(questions)))
        random.shuffle(questions)
        reponse_a()
        question_selection_frame.grid_forget()
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

#programme principal de lancement
def demarrage():
    #si je fais pas ca, ca marche pas
    global title, question_selection_frame, num_questions, start_button, reset_button,question_label,option_buttons,timer_label,timer

#titre
    title = ctk.CTkLabel(root, text="Quiz de Culture Aléatoire", font=("Arial", 35, "bold"), text_color="White")
    title.grid(row=0, column=1, columnspan=2, pady=20, sticky="nsew")

#menu question
    question_selection_frame = ctk.CTkFrame(root)
    question_selection_frame.grid(row=1, column=1, columnspan=2, pady=20, sticky="nsew")

    question_selection_label = ctk.CTkLabel(question_selection_frame, text=f"A combien de questions voulez-vous répondre ? \n(Entre 1 et {str(len(questions))}) ",   font=("Arial", 15), text_color="white")
    question_selection_label.grid(row=0, column=0, padx=10, sticky="nsew")

#numero de selection des questions
    num_questions = ctk.CTkEntry(question_selection_frame, font=("Arial", 16), width=100,justify="center")
    num_questions.grid(row=0, column=1, padx=10, sticky="nsew")

#boutton demarrer
    start_button = ctk.CTkButton(question_selection_frame, text="Démarrer", font=("Arial", 16), command=start_quiz)
    start_button.grid(row=1, column=1, columnspan=1, pady=10)

#boutton reset
    reset_button = ctk.CTkButton(root, text="Réinitialiser", font=("Arial", 25), command=reset_quiz)
    reset_button.grid(row=4, column=1, columnspan=2, pady=10)

#timer
    timer_label = ctk.CTkLabel(root, text=f"Temps restant : {remaining_time} s", font=("Arial", 20), text_color="#FFD700")
    timer_label.grid(row=2, column=1, columnspan=2, pady=10, sticky="nsew")


    question_label = ctk.CTkLabel(root, text="", font=("Arial", 20), wraplength=600, justify="center", text_color="white")


    options_frame = ctk.CTkFrame(root)
    options_frame.grid(row=3, column=1, columnspan=2, pady=20, sticky="nsew")

    option_buttons = {}
    for i in range(2):
        for j in range(2):
            btn = ctk.CTkButton(options_frame, text="", font=("Arial", 14), width=375, height=50, fg_color="#7100cf", hover=False)
            btn.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
            option_buttons[btn] = None





ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Quiz de Culture Aléatoire")
root.geometry("790x600")
root.minsize(600, 400)

current_question = 0
score = 0
remaining_time = 15


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=0)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(3, weight=1)

demarrage()

root.mainloop()

