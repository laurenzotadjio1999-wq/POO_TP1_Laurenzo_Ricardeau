# Classe Adhérent
class Adherent:
    prochain_id = 1

    def __init__(self, nom, prenom):
        self.id = Adherent.prochain_id
        Adherent.prochain_id += 1
        self.nom = nom
        self.prenom = prenom
        self.livres_empruntes = []

    def __str__(self):
        emprunts_str = ", ".join(map(str, self.livres_empruntes))
        return f"ID: {self.id}, Nom: {self.nom} {self.prenom} | Emprunts: [{emprunts_str}]"
