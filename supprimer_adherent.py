
# 2️⃣ Supprimer Adhérent (AVEC AFFICHAGE PRÉALABLE ET VALIDATION FORCÉE)
def supprimer_adherent(self):
    while True:
        # 1. Afficher la liste des adhérents
        self.afficher_adherents(with_pause=False)
        try:
            id_adherent_str = input("\nEntrez l'ID de l'adhérent à supprimer (ou laissez vide pour annuler) : ")
            if not id_adherent_str: break  # Option d'annulation

            id_adherent = int(id_adherent_str)
            adherent = self.liste_adherents.get(id_adherent)

            if not adherent:
                print(f"❌Erreur: Adhérent avec l'ID {id_adherent} non trouvé.")
            elif adherent.livres_empruntes:
                print("❌Erreur: Ce membre a des Livres en cours d'emprunt et ne peut pas être supprimé.")
            else:
                del self.liste_adherents[id_adherent]
                print(f"SUCCÈS✅: Adhérent {adherent.prenom} {adherent.nom} (ID: {id_adherent}) supprimé.")
            self.appliquer_sauvegarde()
            if not demander_continuer("Supprimer Adhérent"): break

        except ValueError:
            # VALIDER ET FORCER LA SAISIE : Ne pas sortir de la boucle de continuité
            print("❌Erreur: L'ID doit être un nombre entier. Veuillez réessayer.")
            # Le 'continue' implicite de la boucle while True s'exécutera
