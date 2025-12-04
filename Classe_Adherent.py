# Classe Adhérent
class Adherent:
    prochain_id = 1001

    def __init__(self, nom, prenom):
        self.id = Adherent.prochain_id
        Adherent.prochain_id += 1
        self.nom = nom
        self.prenom = prenom
        self.livres_empruntes = []

    def __str__(self):
        return f"Adhérent ID: {self.id} | Nom: {self.prenom} {self.nom} | Emprunts: {len(self.livres_empruntes)}"
