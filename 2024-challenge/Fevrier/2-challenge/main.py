class ListePersonnalisee:
    def __init__(self):
        self.elements = []

    def ajouter_element(self, element):
        # Ajoute un élément à la liste personnalisée
        pass 

    def supprimer_element(self, index):
        # Supprime l'élément à l'index spécifié de la liste personnalisée
        pass

    def acces_element(self, index):
        # Retourne l'élément à l'index spécifié de la liste personnalisée
      pass 

    def affichage(self) :
        pass 



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
