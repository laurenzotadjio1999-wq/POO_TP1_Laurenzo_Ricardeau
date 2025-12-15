
from Classe_Document import Document
# Classe Journal qui hérite de Document
class Journal(Document):
    def __init__(self, title, date_parution, maison_publication):
        super().__init__(title)
        self.date_parution = date_parution
        self.nom_auteur = maison_publication
        self.type_document = "JOURNAL"
        self.disponible = True
    # ...
