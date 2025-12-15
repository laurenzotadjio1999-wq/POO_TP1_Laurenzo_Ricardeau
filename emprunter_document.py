from datetime import date
from datetime import datetime
from Class_Emprunt import Emprunt
#Emprunter Document (CORRIGÉ)
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