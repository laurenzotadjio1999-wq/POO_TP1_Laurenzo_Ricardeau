
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