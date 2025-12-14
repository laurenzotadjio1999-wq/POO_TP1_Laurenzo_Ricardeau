
#Méthodes pour afficher les emprunts
def afficher_emprunts(self, with_pause=True):
    print("\n--- HISTORIQUE DÉTAILLÉ DES EMPRUNTS ---")
    if not self.liste_emprunts:
        print("Aucun emprunt n'a été enregistré.")
    else:
        for emprunt in self.liste_emprunts:
            adherent = self.liste_adherents.get(emprunt.adherent_id)
            document = self.liste_documents.get(emprunt.livre_id)

            # Récupération des noms pour un affichage clair
            nom_adherent = f"{adherent.prenom} {adherent.nom}" if adherent else f"Adhérent Inconnu (ID: {emprunt.adherent_id})"
            type_doc = document.type_document if document else "DOCUMENT"
            titre_doc = document.title if document else f"Document Inconnu (ID: {emprunt.livre_id})"

            # Affichage détaillé
            print("-" * 50)
            print(f"Nom de l'adhérent: {nom_adherent}")
            print(f"Document emprunté: {type_doc}, {titre_doc}")
            print(f"Emprunté le: {emprunt.date_emprunt.isoformat()}")
            print(f"Date de retour prévue: {emprunt.date_retour_prevue.isoformat()}")

            # Affichage du statut si l'emprunt est terminé
            if not emprunt.est_actif:
                print(f"Retourné le: {emprunt.date_retour_reelle.isoformat()}")
                print(f"STATUT: Terminé")
            else:
                print(f"STATUT: Actif (À rendre)")

    # La pause est toujours appelée à la fin
    if with_pause:
        input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")