import csv
from copy import deepcopy


##----- Du CSV vers une liste de dictionaires -----##
def importe_csv(nom_fichier):
    with open(nom_fichier, 'r', encoding="utf-8", newline='') as fichier:
        lecteur = csv.DictReader(fichier,  delimiter=',')
        return [dict(ligne) for ligne in lecteur]


##----- D'une liste de dictionnaires vers un fichier CSV -----##
def exporte_csv(nom_table, nom_fichier, ordre):
    with open(nom_fichier, 'w',  encoding="utf-8", newline='') as fichier:
        # Préparation de la table de données
        donnees = csv.DictWriter(fichier, fieldnames=ordre)
        # Écriture de la première ligne (attributs dans l'ordre)
        donnees.writeheader()
        # Ajout de toutes les lignes
        donnees.writerows(nom_table)



##----- Conversion de valeurs d'attributs en entiers -----##
def attributs_entiers(table, tab_attributs):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    tab_attributs - list, tableau de chaîne de caractères étant des clés de cette table
    Sortie: None - Modifie table dans laquelle les clés attributs ont des valeurs entières (fonction à effet de bord)
    """
    for ligne in table:
        for clef, valeur in ligne.items():
            if clef in tab_attributs:
                ligne[clef] = int(valeur)


##----- Conversion de valeurs d'attributs en flottants -----##
def attributs_flottants(table, tab_attributs):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    tab_attributs - list, tableau de chaîne de caractères étant des clés de cette table
    Sortie: None - Modifie table dans laquelle les clés attributs ont des valeurs flottantes (fonction à effet de bord)
    """
    for ligne in table:
        for clef, valeur in ligne.items():
            if clef in tab_attributs:
                ligne[clef] = float(valeur)



##----- Rechercher une valeur d'attribut -----##
def est_presente(table, attribut, valeur):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    attribut - str, chaîne de caractères représentant une des clés
    valeur - doit être du même type que les valeurs de la clé attribut
    Sortie: booléen - True si valeur est présente dans la ligne pour l'attribut sélectionné, False sinon
    """
    for dico in table:
        if dico[attribut] == valeur:
            return True
    return False


##----- Récupération d'une donnée simple -----##
def recupere_valeur(table, attribut1, valeur1, attribut2):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    attribut1, attribut2 - str, chaînes de caractères représentant une des clés
    valeur1 - doit être du même type que les valeurs de la clé attribut1
    Sortie: la valeur de la clé attribut2 de cette ligne,
            None si attribut1 ne prend jamais la valeur valeur1
    """
    for dico in table:
        if dico[attribut1] == valeur1 :
            return dico[attribut2]
    return None


##----- Comptage d'occurences -----##
def compte_valeur(table, attribut, valeur):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    attribut - str, chaînes de caractères représentant une des clés
    valeur - doit être du même type que les valeurs de la clé attribut
    Sortie : le nombre d'occurences de valeur pour la clé attribut
    """
    compteur = 0
    for dico in table:
        if dico[attribut] == valeur :
            compteur += 1
    return compteur



##----- Selection de colonnes -----##
def projection(table, tab_attributs):
    """
    table - list, Table de données représentée par un tableau de dictionnaires ayant les mêmes clés
    tab_attributs - list, tableau de chaînes de caractères représentant des clés
    Sortie: list, extrait de table retreinte aux clés de tab_attributs
    """
    new_table = []
    for dico in table:
        new_dico = {}
        for attribut in dico.keys():
            if attribut in tab_attributs:
                new_dico[attribut] = dico[attribut]
        new_table.append(new_dico)
    return new_table



##----- Fusion (jointure) de tables -----##
def jointure(table1, table2, attribut1, attribut2=None):
    """
    table1, table2 - list, Tables de données représentée par un tableau de dictionnaires ayant les mêmes clés
    attribut1 - str, chaînes de caractères représentant une clé commune aux deux tables
    attribut2 - str, chaînes de caractères représentant la clé commune mais sous un autre nom dans table2
    Sortie: list, fusion de table1 et table2 selon les attributs
    """
    if attribut2 is None:
        attribut2 = attribut1
    new_table = []
    for dico1 in table1:
        for dico2 in table2:
            if dico1[attribut1] == dico2[attribut2]:
                new_dico = deepcopy(dico1)
                for attribut in dico2:
                    if attribut != attribut2:
                         new_dico[attribut] = dico2[attribut]
                new_table.append(new_dico)
    return new_table

