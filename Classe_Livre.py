# Classe Livre (Hérite de Volume)
class Livre(Volume):
    def __init__(self, titre, nom_auteur):
        super().__init__(titre, nom_auteur)
        self.disponible = True

    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Livre - {super().__str__()} | Statut: {statut}"