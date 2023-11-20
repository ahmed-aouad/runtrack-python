mot = input("quel mot?")

for i in range (len(mot)):
    lettre = mot[i]

    if lettre=="e":
        print("j'ai trouvé le e")
        break

    else: i=i+1