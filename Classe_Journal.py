# Classe Journal qui hérite de Document
class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution

    def __str__(self):
        return f"Journal - {super().__str__()} | Paru le: {self.date_parution}"