import csv
from datetime import datetime
from Classe_Livre import Livre
from Class_Emprunt import Emprunt
from Classe_Adherent import Adherent
from Classe_Journal import Journal
from Classe_Document import Document



def charger_donnees(self):
    print("\n--- Démarrage du Chargement des Données ---")


    # A. CHARGEMENT DES ADHÉRENTS
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


    # B. CHARGEMENT DES DOCUMENTS
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
                    doc = Journal(titre, date_parution ,auteur)
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


    # C. CHARGEMENT DES EMPRUNTS
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