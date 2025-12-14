
#méthode pour retourner un document
def retourner_document(self):
    while True:
        self.afficher_adherents(with_pause=False)
        self.afficher_documents(with_pause=False)

        try:
            id_adherent = int(input("\nID Adhérent : "))
            # Renommage en id_document
            id_document = int(input("ID Document à rendre : "))
        except ValueError:
            print("Erreur: Veuillez entrer des ID numériques entiers. Veuillez réessayer.")
            continue

        adherent = self.liste_adherents.get(id_adherent)
        # Renommage en document
        document = self.liste_documents.get(id_document)

        # VÉRIFICATION GÉNÉRALE
        if not adherent or not document:
            print("Erreur: Adhérent ou Document invalide.")
        # VÉRIFICATION : L'adhérent a-t-il vraiment cet ID d'emprunt ?
        elif id_document not in adherent.livres_empruntes:
            print(f"Erreur: L'adhérent {adherent.id} n'a pas emprunté ce document.")
        else:
            # LOGIQUE DE RETOUR
            document.disponible = True
            adherent.livres_empruntes.remove(id_document)

            for emprunt in self.liste_emprunts:
                if emprunt.adherent_id == id_adherent and emprunt.livre_id == id_document and emprunt.est_actif:
                    emprunt.marquer_retourne()
                    break

            print(
                f"SUCCÈS: le document de type {document.type_document} intitulé '{document.title}' a été retourné par {adherent.prenom}.")

        if not demander_continuer("Retour Emprunt"):
            self.appliquer_sauvegarde()
            break