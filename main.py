from forex_python.converter import CurrencyRates

def afficher_liste_devise(liste_devise):
    print("Voici la liste des devises : ")
    for code, nom in liste_devise.items():
        print(f' - {code} = {nom}')


def enregistrer_conversion(depart, arrivee, montant, resultat):
    with open('historique_conversions.txt', 'a') as fichier:
        fichier.write(f"{depart} -> {arrivee} : {montant} -> {resultat:.2f}\n")


def convertisseur():
    c = CurrencyRates()

    liste_devise = {
        "EUR": "EURO",
        "JPY": "YEN",
        "USD": "DOLLAR US", 
        "CAD": "Dollar canadien",
        "THB": "Bath", 
        "GBP": "Livre sterling",
        "CHF": "Franc suisse"
    }

    afficher_liste_devise(liste_devise)

    print()

    devise_source = input("Quelle devise souhaitez-vous convertir ? ")
    somme = float(input("Veuillez entrer la somme à convertir : "))  # Utilisation de float pour permettre des décimales
    devise_cible = input("Quelle devise monétaire souhaitez-vous obtenir ? ")
    
    try:
        resultat = c.convert(devise_source, devise_cible, somme)
        print(f"Résultat de la conversion : {resultat:.2f} {devise_cible}")
        
        # Enregistrer la conversion dans l'historique
        enregistrer_conversion(devise_source, devise_cible, somme, resultat)
        
    except Exception as e:
        print(f"Erreur : {e}")


convertisseur()
