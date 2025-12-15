
from Class_Volume import Volume
# DANS LA CLASSE BandeDessinee
class BandeDessinee(Volume):
    def __init__(self, title, nom_auteur):
        super().__init__(title, nom_auteur)
        self.type_document = "Bande Déssinée"
        self.disponible = True

    # ...