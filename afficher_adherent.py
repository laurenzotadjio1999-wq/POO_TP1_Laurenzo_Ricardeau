
#classe pour afficher la liste des adhérents
def afficher_adherents(self, with_pause=True):
    print("\n👥 --- LISTE DES ADHÉRENTS --- 👥")

    if not self.liste_adherents:
        print("Aucun adhérent enregistré.")
    else:
        print(f"{'ID':<5} | {'NOM':<20} | {'PRÉNOM':<20} | {'EMPRUNTS ACTIFS':<15}")
        print("=" * 70)

        for adherent in self.liste_adherents.values():
            nb_emprunts = len(adherent.livres_empruntes)

            # Utiliser un émoji pour indiquer un prêt actif
            emprunts_str = f"📚 {nb_emprunts} document(s)" if nb_emprunts > 0 else "— Aucun —"

            print(
                f"{adherent.id:<5} | {adherent.nom:<20} | {adherent.prenom:<20} | {emprunts_str:<15}")

        print("=" * 70)
    if with_pause:
        input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")