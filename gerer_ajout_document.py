#fonction pour l'ajout d'un document
from Classe_Journal import Journal
from Classe_Livre import Livre


def gerer_ajout_document(bibliotheque):
    while True:
        print("\n--- CHOIX DU TYPE DE DOCUMENT ---")
        print("1. Livre")
        print("2. Bande Dessinée")
        print("3. Dictionnaire")
        print("4. Journal")

        choix_type = input("Entrez le type (1-4) : ").strip()
        titre = ""  # Initialisation pour éviter l'erreur si choix_type est invalide

        if choix_type in ('1', '2', '3', '4'):
            titre = input("Entrez le Titre du document : ")

            if choix_type == '1':
                auteur = input("Nom de l'Auteur : ")
                bibliotheque.ajouter_document(Livre(titre, auteur))

            elif choix_type == '2':
                auteur = input("Nom de l'Auteur : ")
                bibliotheque.ajouter_document(BandeDessinee(titre, auteur))

            elif choix_type == '3':
                auteur = input("Nom de l'Auteur (ou Inconnu/Divers) : ")
                bibliotheque.ajouter_document(Dictionnaire(titre, auteur))

            elif choix_type == '4':
                date_parution = input("Date de parution (AAAA-MM-JJ) : ").strip()
                maison_publication = input("Maison de publication : ").strip()
                bibliotheque.ajouter_document(Journal(titre, date_parution, maison_publication))

            print(f"SUCCÈS: Document '{titre}' ajouté.")

            if not demander_continuer("Ajouter Document"):
                bibliotheque.appliquer_sauvegarde()
                break
        else:
            print("Choix de type de document invalide.")
            if not demander_continuer("Ajouter Document"):
                break