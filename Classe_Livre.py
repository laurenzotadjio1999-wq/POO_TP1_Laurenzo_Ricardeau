from Class_Volume import Volume

# Classe Livre (Hérite de Volume)
class Livre(Volume):
    def __init__(self, title, nom_auteur):
        super().__init__(title, nom_auteur)
        self.type_document = "LIVRE"

