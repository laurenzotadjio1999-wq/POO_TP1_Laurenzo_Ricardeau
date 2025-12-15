import csv
from datetime import datetime
from datetime import date

from Class_Volume import Volume
from Classe_Adherent import Adherent
from Classe_Journal import Journal
from Classe_Livre import Livre
from Classe_Document import Document
from Class_Emprunt import Emprunt


def demander_continuer(action_nom):
    """
    Demande à l'utilisateur s'il veut répéter l'action ou revenir au menu.
    Retourne True (1) pour continuer, False (2) pour revenir au menu.
    """
    while True:
        #print(f"\n--- Après l'action '{action_nom}' ---")
        choix = input("1 - Répéter cette action\n2 - Retourner au menu principal\nVotre choix (1 ou 2) : ").strip()

        if choix == '1':
            return True
        elif choix == '2':
            return False
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

def attendre_confirmation():
    """Met le programme en pause jusqu'à ce que l'utilisateur appuie sur Entrée."""
    input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")

class BandeDessinee(Volume):
    def __init__(self, title, nom_auteur):
        super().__init__(title, nom_auteur)
        self.type_document = "Bande Déssinée"
        self.disponible = True

    # ...

# DANS LA CLASSE Dictionnaire
class Dictionnaire(Volume):
    def __init__(self, title, nom_auteur):
        super().__init__(title, nom_auteur)
        self.type_document = "DICTIONNAIRE"
        self.disponible = True
    # ...

# Classe Bibliothèque
class Bibliotheque:
    def __init__(self):
        self.liste_documents = {}
        self.liste_adherents = {}
        self.liste_emprunts = []
        self.FICHIER_DOCUMENTS = 'Documents.csv'
        self.FICHIER_ADHERENTS = 'Adherents.csv'
        self.FICHIER_EMPRUNTS = 'Emprunts.csv'


# 1️⃣ Ajouter Adhérent (Pas de changement majeur, car la saisie est déjà en string)
    def ajouter_adherent(self):
        while True:
            print("\n--- Nouvel Adhérent ---")
            nom = input("Nom de l'adhérent : ")
            prenom = input("Prénom de l'adhérent : ")

            nouvel_adherent = Adherent(nom, prenom)
            self.liste_adherents[nouvel_adherent.id] = nouvel_adherent
            print(
                 f"SUCCÈS✅: Adhérent {nouvel_adherent.prenom} {nouvel_adherent.nom} (ID: {nouvel_adherent.id}) ajouté.")
            if not demander_continuer("Ajout Adhérent"):
                self.appliquer_sauvegarde()
            break

        # Méthode utilitaire
    def ajouter_document(self, document):
        self.liste_documents[document.id] = document

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

# 5️⃣ Supprimer Document (AVEC VALIDATION FORCÉE)
    def supprimer_document(self):
        while True:
            # Afficher la liste des documents peut être utile ici aussi
            self.afficher_documents(with_pause=False)

            try:
                id_document_str = input("\nEntrez l'ID du Document à supprimer (ou laissez vide pour annuler) : ")
                if not id_document_str: break

                id_document = int(id_document_str)
                document = self.liste_documents.get(id_document)

                if not document:
                    print(f"❌Erreur: Document avec l'ID {id_document} non trouvé.")
                elif isinstance(document, Livre) and not document.disponible:
                    print("❌Erreur: Ce Livre est actuellement emprunté et ne peut pas être supprimé.")
                else:
                    del self.liste_documents[id_document]
                    print(f"SUCCÈS✅: Le document intitulé '{document.title}' (ID: {id_document}) supprimé.")
                self.appliquer_sauvegarde()
                if not demander_continuer("Supprimer Document"): break

            except ValueError:
                # VALIDER ET FORCER LA SAISIE
                print("❌Erreur: L'ID doit être un nombre entier. Veuillez réessayer.")

 # 7️⃣ Emprunter Document (CORRIGÉ)
    def emprunter_document(self):
        while True:
            print("\n--- ALLONS Y ---")
            # 1. Afficher les listes (pour aider la saisie)
            self.afficher_adherents(with_pause=False)
            self.afficher_documents(with_pause=False)

            # --- DÉBUT SAISIE AVEC VALIDATION ---
            try:
                id_adherent_str = input(
                    "\nEntrez l'ID de l'Adhérent qui emprunte (laissez vide pour annuler) : ").strip()
                if not id_adherent_str: break

                id_adherent = int(id_adherent_str)
                # La variable est renommée en id_document
                id_document = int(input("Entrez l'ID du Document à emprunter : "))

            except ValueError:
                print("❌Erreur: Veuillez entrer des ID numériques entiers. Veuillez réessayer.")
                continue
                # ------------------------------------

                # --- VÉRIFICATIONS GÉNÉRALES ---
            adherent = self.liste_adherents.get(id_adherent)
            # La variable est renommée en document
            document = self.liste_documents.get(id_document)

            if not adherent:
                print("❌Erreur: Adhérent non trouvé.")
            # VÉRIFICATION : L'objet existe-t-il ?
            elif not document:
                print(f"❌Erreur: Document {id_document} non trouvé.")
            # VÉRIFICATION : Est-il disponible ?
            elif not document.disponible:
                print(f"❌Erreur: Ce Document ('{document.title}') est déjà emprunté.")
            else:
                # --- EXÉCUTION DE L'EMPRUNT ---

                # Saisie et validation de la date de retour (inchangé)
                date_ok = False
                date_retour_obj = None
                while not date_ok:
                    date_retour_str = input("Date de retour prévue (AAAA-MM-JJ) : ").strip()
                    try:
                        date_retour_obj = datetime.strptime(date_retour_str, "%Y-%m-%d").date()
                        duree_pret = date_retour_obj - date.today()
                        if duree_pret.days > 5 or duree_pret.days < 0:
                            print(
                                "❌Erreur: La date de retour doit être au maximum 5 jours après aujourd'hui, et ne peut pas être dans le passé.")
                        else:
                            date_ok = True
                    except ValueError:
                        print("❌Erreur de format de date. Utilisez le format AAAA-MM-JJ.")

                # Mise à jour du statut du document et de l'adhérent
                document.disponible = False
                adherent.livres_empruntes.append(
                    id_document)  # Le nom de la liste interne reste pour l'instant 'livres_empruntes'

                # Création de l'objet Emprunt avec la date saisie
                nouvel_emprunt = Emprunt(adherent.id, document.id, date_retour_prevue=date_retour_obj)
                self.liste_emprunts.append(nouvel_emprunt)
                print(
                    f"SUCCÈS✅: {adherent.prenom} a emprunté le/la {document.type_document} intitulé(e) '{document.title}'. Retour prévu le {date_retour_obj.isoformat()}.")
                self.appliquer_sauvegarde()
            # --- LOGIQUE DE CONTINUITÉ ---
            if not demander_continuer("Ajouter Emprunt"):
                self.appliquer_sauvegarde()
                break


# 8️⃣ Retourner Livre (AVEC VALIDATION FORCÉE)
    def retourner_livre(self):  # On pourrait la renommer en retourner_document
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

                print(f"SUCCÈS: le document de type {document.type_document} intitulé '{document.title}' a été retourné par {adherent.prenom}.")

            if not demander_continuer("Retour Emprunt"):
                self.appliquer_sauvegarde()
                break

    # --- MÉTHODES D'AFFICHAGE ---

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

    def afficher_documents(self, with_pause=True):
        # Dictionnaire des émojis par type
        EMOJIS_DOC = {
            "LIVRE": "📖 LIVRE",
            "BD": "💭 BD",
            "DICTIONNAIRE": "📘 DICTIONNAIRE",
            "JOURNAL": "📰 JOURNAL",
        }

        print("\n📚 --- LISTE DES DOCUMENTS --- 📚")

        if not self.liste_documents:
            print("Aucun document enregistré.")
        else:
            # Notez l'ajustement de l'en-tête pour la largeur
            print(f"{'ID':<5} | {'TYPE':<15}  | {'TITRE':<40} | {'AUTEUR/EDITEUR':<20} | {'STATUT':<10}")
            print("=" * 107)  # Ligne de séparation plus visuelle

            for doc in self.liste_documents.values():
                auteur_info = ""
                statut_info = ""

                # Utilisation des émojis
                type_affiche = EMOJIS_DOC.get(doc.type_document, doc.type_document)  # Affiche l'émoji ou le type brut

                # Récupération de l'auteur/éditeur
                if hasattr(doc, 'nom_auteur'):
                    auteur_info = doc.nom_auteur

                # Gestion du statut avec symboles
                if hasattr(doc, 'disponible'):
                    if doc.disponible:
                        statut_info = "✅ Disponible"
                    else:
                        statut_info = "❌ Emprunté"
                else:
                    statut_info = "N/A"

                # Affichage de la ligne
                print(
                    f"{doc.id:<5} | {type_affiche:<15} | {doc.title:<40} | {auteur_info:<20} | {statut_info:<10}")

            print("=" * 107)

        if with_pause:
            input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")

        # DANS LA CLASSE Bibliotheque

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
                print(f"👤Nom de l'adhérent: {nom_adherent}")
                print(f"📓Document emprunté: {type_doc}, {titre_doc}")
                print(f"📆Emprunté le: {emprunt.date_emprunt.isoformat()}")
                print(f"📆Date de retour prévue: {emprunt.date_retour_prevue.isoformat()}")

                # Affichage du statut si l'emprunt est terminé
                if not emprunt.est_actif:
                    print(f"Retourné le: {emprunt.date_retour_reelle.isoformat()}")
                    print(f"STATUT: Terminé")
                else:
                    print(f"STATUT: Actif (À rendre)")

        # La pause est toujours appelée à la fin
        if with_pause:
            input("\nAppuyez sur ENTRÉE pour continuer et revenir au menu principal...")

    # --- PERSISTANCE (Squelettes) ---
    def sauvegarder_donnees(self):
        """Sauvegarde les données des adhérents, documents et emprunts dans des fichiers CSV."""

        print("\n--- Démarrage de la Sauvegarde des Données ---")
        # ----------------------------------------------------
        # A. SAUVEGARDE DES ADHÉRENTS
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_ADHERENTS, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # En-tête du fichier
                writer.writerow(['ID', 'Nom', 'Prenom', 'Emprunts_IDs'])

                for adherent in self.liste_adherents.values():
                    # Les IDs des documents empruntés sont stockés en tant que chaîne séparée par des virgules
                    emprunts_str = ",".join(map(str, adherent.livres_empruntes))
                    writer.writerow([
                        adherent.id,
                        adherent.nom,
                        adherent.prenom,
                        emprunts_str
                    ])
            print(f"SUCCÈS: {len(self.liste_adherents)} adhérents sauvegardés dans {self.FICHIER_ADHERENTS}")
        except Exception as e:
            print(f"ÉCHEC: Erreur lors de la sauvegarde des adhérents: {e}")

        # ----------------------------------------------------
        # B. SAUVEGARDE DES DOCUMENTS (Plus complexe en raison des différents types)
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_DOCUMENTS, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # NOUVEL EN-TÊTE : 'Dessinateur' est retiré
                writer.writerow(['ID', 'Type', 'Titre', 'Auteur', 'DateParution', 'Disponible'])

                for doc in self.liste_documents.values():
                    # Initialisation des champs spécifiques à None ou vide
                    auteur = ''
                    # dessinateur est retiré
                    date_parution = ''
                    disponible = ''

                    # Logique unifiée : Volume utilise Auteur, Journal utilise DateParution ET Auteur (pour la Maison)
                    if isinstance(doc, Volume) or isinstance(doc, Journal):
                        # Récupère l'auteur du Livre/BD/Dico OU la Maison du Journal
                        if hasattr(doc, 'nom_auteur'):
                            auteur = doc.nom_auteur
                    # La condition BandeDessinee est retirée
                    if isinstance(doc, Journal):
                        date_parution = doc.date_parution

                    if hasattr(doc, 'disponible'):
                        disponible = doc.disponible

                    # NOUVEAU ROW : 'Dessinateur' est retiré
                    writer.writerow([
                        doc.id,
                        doc.type_document,
                        doc.title,
                        auteur,
                        date_parution,  # Le champ Dessinateur n'est plus là
                        disponible
                    ])
            print(f"SUCCÈS: {len(self.liste_documents)} documents sauvegardés dans {self.FICHIER_DOCUMENTS}")
        except Exception as e:
            print(f"ÉCHEC: Erreur lors de la sauvegarde des documents: {e}")

        # ----------------------------------------------------
        # C. SAUVEGARDE DES EMPRUNTS
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_EMPRUNTS, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Adherent_ID', 'Livre_ID', 'Date_Emprunt', 'Date_Retour_Prevue', 'Date_Retour_Reelle',
                                 'Est_Actif'])

                for emprunt in self.liste_emprunts:
                    # Convertir les dates en chaînes (ISO format)
                    date_reel = emprunt.date_retour_reelle.isoformat() if emprunt.date_retour_reelle else ''

                    writer.writerow([
                        emprunt.adherent_id,
                        emprunt.livre_id,
                        emprunt.date_emprunt.isoformat(),
                        emprunt.date_retour_prevue.isoformat(),
                        date_reel,
                        emprunt.est_actif
                    ])
            print(f"SUCCÈS: {len(self.liste_emprunts)} emprunts sauvegardés dans {self.FICHIER_EMPRUNTS}")
        except Exception as e:
            print(f"ÉCHEC: Erreur lors de la sauvegarde des emprunts: {e}")


    def charger_donnees(self):
        print("\n--- Démarrage du Chargement des Données ---")

        # ----------------------------------------------------
        # A. CHARGEMENT DES ADHÉRENTS
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_ADHERENTS, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Sauter l'en-tête

                max_id = 0
                for row in reader:
                    adherent_id = int(row[0])
                    nom, prenom = row[1], row[2]
                    emprunts_ids_str = row[3]

                    # Créer l'objet Adherent sans utiliser le compteur interne
                    adh = Adherent(nom, prenom)
                    adh.id = adherent_id

                    # Reconstruire la liste des emprunts
                    if emprunts_ids_str:
                        adh.livres_empruntes = [int(i) for i in emprunts_ids_str.split(',')]

                    self.liste_adherents[adherent_id] = adh
                    max_id = max(max_id, adherent_id)

                # Réinitialiser le compteur d'ID pour éviter les doublons
                Adherent.prochain_id = max_id + 1

            print(f"SUCCÈS: {len(self.liste_adherents)} adhérents chargés.")
        except FileNotFoundError:
            try:
                with open(self.FICHIER_ADHERENTS, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['ID', 'Nom', 'Prenom', 'Emprunts_IDs'])
                print(f"AVERTISSEMENT: Fichier {self.FICHIER_ADHERENTS} créé avec en-tête.")
            except Exception as e:
                print(f"ÉCHEC CRÉATION: Impossible de créer {self.FICHIER_ADHERENTS}: {e}")

        except Exception as e:
                print(f"ÉCHEC: Erreur lors du chargement des adhérents: {e}")

        # ----------------------------------------------------
        # B. CHARGEMENT DES DOCUMENTS
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_DOCUMENTS, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Sauter l'en-tête

                max_id = 0
                for row in reader:
                    # [ID, Type, Titre, Auteur, DateParution, Disponible]
                    doc_id, doc_type, titre, auteur, date_parution, disponible_str = row
                    doc_id = int(doc_id)

                    # Reconstruire l'objet en fonction de son type
                    if doc_type == 'LIVRE':
                        doc = Livre(titre, auteur)
                    elif doc_type == 'BD':
                        # CONSTRUCTEUR MISE À JOUR : sans 'dessinateur'
                        doc = BandeDessinee(titre, auteur)
                    elif doc_type == 'DICTIONNAIRE':
                        doc = Dictionnaire(titre, auteur)
                    elif doc_type == 'JOURNAL':
                        doc = Journal(titre, date_parution,auteur)
                    else:
                        continue

                        # L'attribut 'disponible' est universel
                    if hasattr(doc, 'disponible'):
                        doc.disponible = (disponible_str == 'True')

                    doc.id = doc_id
                    self.liste_documents[doc_id] = doc
                    max_id = max(max_id, doc_id)

                Document.id_suivant = max_id + 1

            print(f"SUCCÈS: {len(self.liste_documents)} documents chargés.")
        except FileNotFoundError:

            try:
                with open(self.FICHIER_DOCUMENTS, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['ID', 'Type', 'Titre', 'Auteur', 'DateParution', 'Disponible'])
                print(f"AVERTISSEMENT: Fichier {self.FICHIER_DOCUMENTS} créé avec en-tête.")
            except Exception as e:
                print(f"ÉCHEC CRÉATION: Impossible de créer {self.FICHIER_DOCUMENTS}: {e}")

        except Exception as e:
                print(f"ÉCHEC: Erreur lors du chargement des documents: {e}")

        # ----------------------------------------------------
        # C. CHARGEMENT DES EMPRUNTS
        # ----------------------------------------------------
        try:
            with open(self.FICHIER_EMPRUNTS, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Sauter l'en-tête

                for row in reader:
                    # ['Adherent_ID', 'Livre_ID', 'Date_Emprunt', 'Date_Retour_Prevue', 'Date_Retour_Reelle', 'Est_Actif']
                    ad_id, doc_id, date_emprunt_str, date_prevue_str, date_reel_str, actif_str = row

                    # Conversion des dates
                    date_emprunt = datetime.strptime(date_emprunt_str, "%Y-%m-%d").date()
                    date_prevue = datetime.strptime(date_prevue_str, "%Y-%m-%d").date()
                    date_reel = datetime.strptime(date_reel_str, "%Y-%m-%d").date() if date_reel_str else None

                    # Création de l'objet Emprunt
                    emprunt = Emprunt(
                        int(ad_id),
                        int(doc_id),
                        date_emprunt,
                        date_prevue,
                        date_reel,
                        actif_str == 'True'
                    )
                    self.liste_emprunts.append(emprunt)

            print(f"SUCCÈS: {len(self.liste_emprunts)} emprunts chargés.")
        except FileNotFoundError:
            try:
                with open(self.FICHIER_EMPRUNTS, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        ['Adherent_ID', 'Livre_ID', 'Date_Emprunt', 'Date_Retour_Prevue', 'Date_Retour_Reelle',
                         'Est_Actif'])
                print(f"AVERTISSEMENT: Fichier {self.FICHIER_EMPRUNTS} créé avec en-tête.")
            except Exception as e:
                print(f"ÉCHEC CRÉATION: Impossible de créer {self.FICHIER_EMPRUNTS}: {e}")

        except Exception as e:
                print(f"ÉCHEC: Erreur lors du chargement des emprunts: {e}")

    def appliquer_sauvegarde(self):
        """Appelle la sauvegarde complète pour mettre à jour les fichiers."""
        self.sauvegarder_donnees()


# ==============================================================================
# PROGRAMME PRINCIPAL ET MENU
# ==============================================================================

def afficher_menu():
    """Affiche les options disponibles pour le gestionnaire."""
    print("\n" + "=" * 55)
    print("**       📚 Bienvenue à votre bibliothèque 📚        **")
    print("**       👉 Faites un choix :                        **")
    print("=" * 55)
    print("** 1️⃣      Ajouter adhérent                          **")
    print("** 2️⃣      Supprimer adhérent                        **")
    print("** 3️⃣      Afficher tous les adhérents               **")
    print("** 4️⃣      Ajouter Document                          **")
    print("** 5️⃣      Supprimer Document                        **")
    print("** 6️⃣      Afficher tous les Documents               **")
    print("** 7️⃣      Ajouter Emprunt (Prêt d'un Livre)         **")
    print("** 8️⃣      Retour d’un Emprunt (Rendre un Livre)     **")
    print("** 9️⃣      Afficher tous les Emprunts                **")
    print("** Q       Quitter                                   **")
    print("*" * 55)


def gerer_ajout_document(bibliotheque):
    """Gère l'interaction pour ajouter un nouveau document AVEC BOUCLE."""
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
               # dessinateur = input("Nom du Dessinateur : ")
                bibliotheque.ajouter_document(BandeDessinee(titre, auteur))

            elif choix_type == '3':
                auteur = input("Nom de l'Auteur (ou Inconnu/Divers) : ")
                bibliotheque.ajouter_document(Dictionnaire(titre, auteur))

            elif choix_type == '4':
                date_parution = input("Date de parution (AAAA-MM-JJ) : ").strip()
                maison_publication = input("Maison de publication : ").strip()
                bibliotheque.ajouter_document(Journal(titre, date_parution, maison_publication))

            print(f"SUCCÈS✅: Document '{titre}' ajouté.")

            if not demander_continuer("Ajouter Document"):
                bibliotheque.appliquer_sauvegarde()
                break
        else:
            print("Choix de type de document invalide.")
            if not demander_continuer("Ajouter Document"):
                break
