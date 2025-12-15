# Classe Emprunt
from datetime import date

class Emprunt:
    def __init__(self, adherent_id, livre_id, date_emprunt=date.today(),
                 date_retour_prevue=None,
                 date_retour_reelle=None, est_actif=True):
        self.adherent_id = adherent_id
        self.livre_id = livre_id
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_reelle = date_retour_reelle
        self.est_actif = est_actif

    def marquer_retourne(self):
        self.date_retour_reelle = date.today()
        self.est_actif = False

    def __str__(self):
        statut = "Actif" if self.est_actif else "Terminé"
        retour = self.date_retour_reelle.isoformat() if self.date_retour_reelle else "N/A"
        return f"Emprunt (ID A:{self.adherent_id}, ID L:{self.livre_id}) | Du: {self.date_emprunt.isoformat()} | Retour: {retour} | Statut: {statut}"

