# AFFICHER menu [cyan, magenta, jaune]
print("""
Les couleurs disponibles pour le mélange sont : 
cyan
magenta
jaune

*** Ne choisissez pas deux fois la même couleur ! ***
""")

#  LIRE les choix
couleur1 = input("Quel est la première couleur choisie ? ")
couleur2 = input("Quel est la deuxième couleur choisie ? ")

# Mettre de l'espace dans l'affichage.
print()

# TROUVER le résultat du mélange
if (couleur1 == "cyan" and couleur2 == "magenta") \
        or (couleur1 == "magenta" and couleur2 == "cyan"):
    melange = "violet"

elif (couleur1 == "magenta" and couleur2 == "jaune") \
        or (couleur1 == "jaune" and couleur2 == "magenta"):
    melange = "orange"

else:
    melange = "vert"

# AFFICHER le résultat du mélange
print(f"Le résultat du mélange est {melange}.")
