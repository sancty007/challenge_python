class Chien:
    def __init__(self, race):
        self.race = race

class Chihuahua(Chien):
    def __init__(self, nom):
        self.nom = nom

chien = Chihuahua("Lily")
print(chien.race)