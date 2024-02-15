class ListePersonnalisee:
    def __init__(self):
        self.elements = []

    def ajouter_element(self, element):
        # Ajoute un élément à la liste personnalisée
        self.elements.append(element)

    def supprimer_element(self, index):
        # Supprime l'élément à l'index spécifié de la liste personnalisée
        if index >= 0 :
            del self.elements[index]
        else :
            print("index hors de n'autre liste ! ")

    def acces_element(self, index):
        # Retourne l'élément à l'index spécifié de la liste personnalisée
        if index >= 0 :
            return self.elements[index]
        else :
            print("index hors de n'autre liste ! ")

    def affichage(self) :
        for i in range(len(self.elements)):
            print(self.acces_element(i))



# Exemple d'utilisation
liste = ListePersonnalisee()
liste.ajouter_element("Bonjour")
liste.ajouter_element("tout")
liste.ajouter_element("le")
liste.ajouter_element("monde")

liste.affichage()


print(liste.acces_element(0))  # Devrait afficher "Bonjour"
liste.supprimer_element(1)
print(liste.acces_element(1))  # Devrait afficher "le"
