from fonctions_csv import*
import random

## Parametre
lexique = importe_csv('lexique.csv')
lexique=set(map(lambda x: x['0'], lexique))

## Génération

def generation():
    mot = random.choice(tuple(lexique))
    return mot

def majuscule(mot_généré):
    transition = ''
    for elt in mot_généré:
        transition+=chr(ord(elt)-32)
    return transition

## Proposition

def proposition(connues):
    print(f'{connues} ({len(réponse)})')
    prop=str(input('Nouvelle Proposition : '))
    while len(prop)!=len(réponse) or prop not in lexique:
        if len(prop)!=len(réponse):
            prop=str(input(f'Nombre de lettres differents ({len(prop)})! Réessaye : '))
        if prop not in lexique:
            prop=str(input(f'Nous ne connaissons pas ce mot ! Réessaye : '))
    return prop

## Vérification

def verification(prop, réponse):
    vérif = ['/' for elt in réponse]
    cpt_reponse = {}
    for elt in réponse:
        cpt_reponse[elt] = cpt_reponse.get(elt,0) + 1
    for i, elem in enumerate(prop):
        if elem == réponse[i]:
            vérif[i] = '='
            cpt_reponse[elem] = cpt_reponse.get(elt,0) - 1
    for i, elem in enumerate(prop):
        if vérif[i] != '=' and cpt_reponse.get(elem, 0) != 0:
            vérif[i] = '~'
            cpt_reponse[elem] = cpt_reponse.get(elem, 0) - 1
    return vérif

def connaissance(vérif, réponse, connues):
    nouveau=''
    for i, elt in enumerate(vérif):
        if elt == '=' :
            nouveau+=réponse[i]
        else:
            nouveau+=connues[i]
    return nouveau

## Affichage & Main

def affichage(prop, verif):
    cases=[prop, verif]
    largeur = len(cases[0])
    print("  ", end="")
    for i in range(1, largeur+1):
        num = str(i)
        k = True
        while len(num) < 5:
            if k:
                num = " " + num
            else:
                num = num + " "
            k = not(k)
        print(" "+num, end="")
    print()

    print("   "+"_"*(largeur*(6)-1))
    for ligne in cases:
        print("  |"+(" "*5+"|")*largeur)
        print("  |", end="")
        for element in ligne:
            carac = element
            k = True
            while len(carac) < 3:
                if k:
                    carac = " " + carac
                else:
                    carac = carac + " "
                k = not(k)
            print(" "+carac+" |", end="")
        print()
        print("  |"+("_"*(5)+"|")*largeur)
    print()

if __name__ == '__main__':
    max_tour = 6
    prop = ''
    tour = 1
    réponse=majuscule(generation())
    connues = réponse[0] + ('-' * (len(réponse)-1))
    while connues!=réponse and tour < max_tour and prop!=réponse:
        prop=majuscule(proposition(connues))
        verif=verification(prop, réponse)
        connues=connaissance(verif, réponse, connues)
        affichage(prop, verif)
        tour+=1
    if tour == max_tour:
        print("VOus avez perdu..")
    else:
        print('GG!')
