

from Classe_Journal import Journal
from Class_Volume import Volume

def afficher_documents(self, with_pause=True):
    print("\n--- LISTE DES DOCUMENTS ---")
    if not self.liste_documents:
        print("Aucun document enregistré.")
    else:
        print(f"{'ID':<5} | {'TYPE':<15} | {'TITRE':<40} | {'AUTEUR':<20} | {'STATUT':<10}")
        print("-" * 105)

        for doc in self.liste_documents.values():
            auteur_info = ""
            statut_info = ""

            if isinstance(doc, Volume):
                auteur_info = doc.nom_auteur
            if isinstance(doc, Journal):
                auteur_info = doc.nom_auteur

            # STATUT DE DISPONIBILITÉ POUR TOUS LES DOCUMENTS QUI ONT L'ATTRIBUT
            if hasattr(doc, 'disponible'):
                statut_info = "Disponible" if doc.disponible else "Emprunté"
            else:
                statut_info = "N/A"  # Au cas où un document de base n'a pas l'attribut.

            print(
                f"{doc.id:<5} | {doc.type_document:<15} | {doc.title:<40} | {auteur_info:<20} | {statut_info:<10}")

    if with_pause:
        input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")
