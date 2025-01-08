#Saisie des Noms et Notes
noms_etudiants = []
notes_etudiants = []

# Demande du nombre d'étudiants à saisir
nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))

for i in range(1, nombre_etudiants + 1):
    nom = input(f"Nom de l’étudiant {i} : ")
    while True:
        try:
            note = float(input(f"Note de {nom} (sur 20) : "))
            if 0 <= note <= 20:  # Vérifie que la note est dans l'intervalle valide
                break
            else:
                print("Erreur : la note doit être comprise entre 0 et 20.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide pour la note.")
    noms_etudiants.append(nom)
    notes_etudiants.append(note)

# Affichage des données saisies pour vérification
print("\nÉtudiants et leurs notes :")
for i in range(nombre_etudiants):
    print(f"{noms_etudiants[i]} : {notes_etudiants[i]}/20")