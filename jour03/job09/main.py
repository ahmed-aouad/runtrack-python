def moyenne(note1, note2, note3):
    return (note1 + note2 + note3)/3

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : ")) 

moyenne_eleve= moyenne(note1, note2, note3)

print(moyenne_eleve)

if  15 <= moyenne_eleve <= 20:
    print("Très bon élève")

if  11 <= moyenne_eleve < 15:
    print("Bon éleve")

if  8 <= moyenne_eleve < 11:
    print("Eleve moyen")

if  0 <= moyenne_eleve < 8:
    print("Élève devant faire des efforts") 

    

    



