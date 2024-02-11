

resultat = "bonjour-tout-le-monde"


# Initialiser l'indice de départ pour le découpage


def separateur(variable , char):
 
    tableau = []  # Initialiser la liste pour stocker les parties séparées
    indice_depart = 0

    for i in range(len(variable)):
        phrase = ''
        if variable[i] == char:
            phrase = variable[indice_depart:i] # interation jusqu'a la rencontre d'un tiret 

            indice_depart = i + 1

            tableau.append(phrase)

    tableau.append(resultat[indice_depart:])

    return tableau




resultat = separateur("bonjour-tout-le-monde", "-")

print(resultat)