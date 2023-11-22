def variété(type, saison):
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine et kiwi")

    if type == "fruits" and saison == "été" :
        print("Poire, fraise, cassis")

    if type == "legume" and saison == "hiver" :  
        print("carotte, topinambour, endive")  

    if type == "legume" and saison == "été" :   
        print("artichaut, aubergine,navet") 

variété("fruits", "hiver")   
variété("fruits", "été") 
variété("legume", "hiver")  
variété("legume", "été")  
