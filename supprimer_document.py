# Méthode aupprimer document
from Classe_Livre import Livre


def supprimer_document(self):
    while True:
        # Afficher la liste des documents afin de choisir celui qu'il faut supprimer
        self.afficher_documents(with_pause=False)

        try:
            id_document_str = input("\nEntrez l'ID du Document à supprimer (ou laissez vide pour annuler) : ")
            if not id_document_str: break

            id_document = int(id_document_str)
            document = self.liste_documents.get(id_document)

            if not document:
                print(f"Erreur: Document avec l'ID {id_document} non trouvé.")
            elif isinstance(document, Livre) and not document.disponible:
                print("Erreur: Ce Livre est actuellement emprunté et ne peut pas être supprimé.")
            else:
                del self.liste_documents[id_document]
                print(f"SUCCÈS: Le document intitulé '{document.title}' (ID: {id_document}) supprimé.")
            self.appliquer_sauvegarde()
            if not demander_continuer("Supprimer Document"): break

        except ValueError:
            # Validation de la saisie utilisateur
            print("Erreur: L'ID doit être un nombre entier. Veuillez réessayer.")
