# Classe Document
class Document:
    # 1. CORRECTION: Définir le compteur statique au niveau de la classe
    id_suivant = 1

    def __init__(self, title):
        self.id = Document.id_suivant
        Document.id_suivant += 1
        self.title = title
    def __str__(self):
        return f"ID: {self.id} | Titre: {self.title}"