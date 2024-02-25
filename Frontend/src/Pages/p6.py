def convertisseur_devise():
    taux_conversion = 10.03

    try:
        montant_usd = float(input("Entrez le montant (USD) : "))
        montant_mad = montant_usd * taux_conversion

        print(f"Montant converti : {montant_mad:.2f} MAD")
    except ValueError:
        print("Veuillez entrer un montant valide.")

convertisseur_devise()
