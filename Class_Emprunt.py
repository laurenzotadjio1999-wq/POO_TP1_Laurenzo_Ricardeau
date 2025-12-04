# Classe Emprunt
class Emprunt:
    def __init__(self, adherent, livre):
        self.adherent_id = adherent.id
        self.livre_id = livre.id
        self.date_emprunt = date.today()
        self.date_retour_prevue = None
        self.date_retour_reelle = None
        self.est_actif = True

    def marquer_retourne(self):
        self.date_retour_reelle = date.today()
        self.est_actif = False

    def __str__(self):
        statut = "Actif" if self.est_actif else "Terminé"
        return f"Emprunt {statut} | Adhérent ID: {self.adherent_id} | Livre ID: {self.livre_id} | Date Prêt: {self.date_emprunt}"