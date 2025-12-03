# Classe Volume qui hérite de Document
class Volume(Document):
    def __init__(self, titre, nom_auteur):
        super().__init__(titre)
        self.nom_auteur = nom_auteur

    def __str__(self):
        return f"{super().__str__()} | Auteur: {self.nom_auteur}"