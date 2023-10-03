# VARIABLES :
prix_batterie = 120
prix_badminton = 60
prix_cheerleading = 90
prix_equitation = 300
prix_cirque = 160
budget = 400
prix_total = 0

# AFFICHER menu des cours de Réguinguin
print("""Cours disponibles pour Réguinguin : 
1 - Batterie
2 - Badminton
3 - Cheerleading
""")

# LIRE choix de Réguinguin
choix_1 = input("Quel cours choisis-tu Réguinguin ? ")

# AFFICHER menu des cours de Clapoche
print("""\nCours disponibles pour Clapoche : 
1 - Équitation
2 - Arts du cirques
""")

# LIRE choix de Clapoche
choix_2 = input("Quel cours choisis-tu Clapoche ? ")

# CALCULER total des 2 cours
if choix_1 == "1":
    if choix_2 == "1":
        prix_total = prix_batterie + prix_equitation
    else:
        prix_total = prix_batterie + prix_cirque
elif choix_1 == "2":
    if choix_2 == "1":
        prix_total = prix_badminton + prix_equitation
    else:
        prix_total = prix_badminton + prix_cirque
else:
    if choix_2 == "1":
        prix_total = prix_cheerleading + prix_equitation
    else:
        prix_total = prix_cheerleading + prix_cirque

    # CALCULER budget restant
budget_restant = budget - prix_total

# AFFICHER activité supplémentaire selon le budget restant
if budget_restant >= 80:
    print(f"\nLes 2 activités coûtent {prix_total:.2f} $, on va au parc de trampoline!")
elif budget_restant >= 40:
    print(f"\nLes 2 activités coûtent {prix_total:.2f} $, on va aller au cinéma!")
elif budget_restant >= 10:
    print(f"\nLes 2 activités coûtent {prix_total:.2f} $, on va s'acheter une crème glacée!")
elif budget_restant < 0:
    print(f"\nLes 2 activités coûtent {prix_total:.2f} $, c'est trop!")


