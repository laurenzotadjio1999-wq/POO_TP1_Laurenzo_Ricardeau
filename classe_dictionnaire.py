from Class_Volume import Volume
#classe dictionnaire
class Dictionnaire(Volume):
    def __init__(self, title, nom_auteur):
        super().__init__(title, nom_auteur)
        self.type_document = "DICTIONNAIRE"
        self.disponible = True
    # ...