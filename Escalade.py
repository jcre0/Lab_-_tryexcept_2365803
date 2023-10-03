# Variables
import sys

prix_unite = None
prix_1_mois = 95.00
prix_3_mois = 265.00
prix_6_mois = 430.00
prix_12_mois = 695.00
pourcent_taxe = 0.14975


try:  # This part of the code will verify if the entered value is a positive number. If not, the program ends.
    prix_unite = float(input("Entrer le prix par unité: "))
    if prix_unite < 0:
        raise ValueError()
    else:
        print()
except ValueError or TypeError:
    sys.exit("Entrer un chiffre positif seulement.")



try:
    # LIRE le nombre de mois d'abonnement
    nb_mois_abonnement = input("Pour combien de mois désirez-vous vous abonner [1, 3, 6, 12] ? ")

    if nb_mois_abonnement == "1":
        # CALCULER nb fois par semaine pour 1 mois.
        nb_fois_sem = (prix_1_mois / prix_unite) / 4.33

        # CALCULER le prix réel par visite - 2 fois semaine avec abonnement 12 mois.
        prix_reel_2_fois_sem = (prix_1_mois + (prix_1_mois * pourcent_taxe)) / (4.33 * 2)

    elif nb_mois_abonnement == "3":
        # CALCULER nb fois par semaine pour 3 mois.
        nb_fois_sem = (prix_3_mois / prix_unite) / 13

        # CALCULER le prix réel par visite - 2 fois semaine avec abonnement 12 mois.
        prix_reel_2_fois_sem = (prix_3_mois + (prix_3_mois * pourcent_taxe)) / (13 * 2)

    elif nb_mois_abonnement == "6":
        # CALCULER nb fois par semaine pour 6 mois.
        nb_fois_sem = (prix_6_mois / prix_unite) / 26

        # CALCULER le prix réel par visite - 2 fois semaine avec abonnement 12 mois.
        prix_reel_2_fois_sem = (prix_6_mois + (prix_6_mois * pourcent_taxe)) / (26 * 2)

    elif nb_mois_abonnement =="12":
        # CALCULER nb fois par semaine pour 12 mois.
        nb_fois_sem = (prix_12_mois / prix_unite) / 52

        # CALCULER le prix réel par visite - 2 fois semaine avec abonnement 12 mois.
        prix_reel_2_fois_sem = (prix_12_mois + (prix_12_mois * pourcent_taxe)) / (52 * 2)
    else:
        raise ValueError()
except ValueError:
    sys.exit("L'entré de l'utilisateur n'est pas bonne.")

# AFFICHER nombre de fois par semaine pour être rentable
print(f"\nCombien de fois par semaine doit-il aller au gym " +
f"avec un abonnement {nb_mois_abonnement} mois ?")
print(f"Il doit y aller {nb_fois_sem:.1f} fois par semaine.")

# AFFICHER le coût réel par visite s'il y va 2 fois par semaine.
print(f"\nÀ combien est-ce que ça lui revient par visite s’il " +
f"va à l’escalade 2 fois par semaines ?")
print(f"Chaque visite lui coûte réellement : {prix_reel_2_fois_sem:.2f} $ taxes incluses.")
