# Classe Bibliothèque
class Bibliotheque:
    def __init__(self):
        self.liste_documents = {}
        self.liste_adherents = {} # CORRECTION: Utiliser le pluriel et la minuscule pour la cohérence
        self.liste_emprunts = []