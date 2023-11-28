def arrondir_notes(notes):
    notes_arrondies = []
    for i in notes:
        if i < 40:
            notes_arrondies.append(i)  # Étudiant a échoué donc pas d'arrondi
        else:
            multiple_de_5_superieur = (i // 5 + 1) * 5
            if multiple_de_5_superieur - i < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(i)  

    return notes_arrondies

# Exemple d'utilisation
liste_notes = [31, 80, 64, 91, 43]
resultat = arrondir_notes(liste_notes)
print(resultat)