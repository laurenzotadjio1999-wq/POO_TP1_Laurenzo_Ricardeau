import csv
from Class_Volume import Volume
from Classe_Journal import Journal


def sauvegarder_donnees(self):
    #Sauvegarde les données des adhérents, documents et emprunts dans des fichiers CSV.#

    print("\n--- Démarrage de la Sauvegarde des Données ---")

    # A. SAUVEGARDE DES ADHÉRENTS

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


    # B. SAUVEGARDE DES DOCUMENTS

    try:
        with open(self.FICHIER_DOCUMENTS, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            #  EN-TÊTE DU FICHIER :
            writer.writerow(['ID', 'Type', 'Titre', 'Auteur', 'DateParution', 'Disponible'])

            for doc in self.liste_documents.values():
                # Initialisation des champs spécifiques à None ou vide
                auteur = ''
                date_parution = ''
                disponible = ''

                # Logique unifiée : Volume utilise Auteur, Journal utilise DateParution ET Auteur (pour la Maison)
                if isinstance(doc, Volume) or isinstance(doc, Journal):
                    # Récupère l'auteur du Livre/BD/Dico OU la Maison du Journal
                    if hasattr(doc, 'nom_auteur'):
                        auteur = doc.nom_auteur

                if isinstance(doc, Journal):
                    date_parution = doc.date_parution

                if hasattr(doc, 'disponible'):
                    disponible = doc.disponible


                writer.writerow([
                    doc.id,
                    doc.type_document,
                    doc.title,
                    auteur,
                    date_parution,
                    disponible
                ])
        print(f"SUCCÈS: {len(self.liste_documents)} documents sauvegardés dans {self.FICHIER_DOCUMENTS}")
    except Exception as e:
        print(f"ÉCHEC: Erreur lors de la sauvegarde des documents: {e}")


    # C. SAUVEGARDE DES EMPRUNTS
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
