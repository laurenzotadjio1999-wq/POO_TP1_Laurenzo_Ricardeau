# Classe Bibliothèque
class Bibliotheque:
    def __init__(self):
        self.liste_documents = {}
        self.liste_adherents = {}
        self.liste_emprunts = []
        self.FICHIER_DOCUMENTS = 'Documents.csv'
        self.FICHIER_ADHERENTS = 'Adherents.csv'
        self.FICHIER_EMPRUNTS = 'Emprunts.csv'