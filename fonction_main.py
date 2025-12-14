


from Classe_Adherent import Adherent



def main():
    bibliotheque = Bibliotheque()
    # --- CHARGEMENT DES DONNÉES AU DÉMARRAGE ---
    bibliotheque.charger_donnees()
    # --- Création de données initiales de test ---
    # Si aucun fichier n'existait, vous pouvez réactiver l'initialisation pour les tests :
    if not bibliotheque.liste_adherents:
        adherent_initial = Adherent("Test", "Gestionnaire")
        bibliotheque.liste_adherents[adherent_initial.id] = adherent_initial
        # ... (ajouter d'autres documents initiaux si nécessaire)
        print("Initialisation: Données de test ajoutées car les fichiers étaient vides/absents.")

    # -----------------------------------------------------------------------------------------

    while True:
        afficher_menu()
        choix = input("Choisissez une action : ").strip().upper()

        if choix == '1':
            bibliotheque.ajouter_adherent()
        elif choix == '2':
            bibliotheque.supprimer_adherent()
        elif choix == '3':
            bibliotheque.afficher_adherents()
        elif choix == '4':
            gerer_ajout_document(bibliotheque)
        elif choix == '5':
            bibliotheque.supprimer_document()
        elif choix == '6':
            bibliotheque.afficher_documents()
        elif choix == '7':
            bibliotheque.emprunter_document()
        elif choix == '8':
            bibliotheque.retourner_livre()
        elif choix == '9':
            bibliotheque.afficher_emprunts()
        elif choix == 'Q':
            print("Fermeture du logiciel...")
            bibliotheque.sauvegarder_donnees()  # <-- SAUVEGARDE À LA SORTIE
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

if __name__ == '__main__':
    main()