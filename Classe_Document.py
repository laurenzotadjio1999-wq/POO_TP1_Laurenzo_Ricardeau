# Classe Document
class Document:
    id_suivant = 1
    def __init__(self, title):
        self.id = Document.id_suivant
        Document.id_suivant += 1
        self.title = title
        self.type_document = "DOCUMENT"
        self.disponible = True