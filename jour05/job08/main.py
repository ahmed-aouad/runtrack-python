def my_sort(lst):
    n = len(lst)  
    coups = 0  

    for i in range(n):
       
        for j in range(0, n-i-1):
           
            if lst[j] > lst[j+1]:
               
                lst[j], lst[j+1] = lst[j+1], lst[j]
                coups += 1 

   
    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")

    return lst  

ma_liste = [11, 80, 22, 25, 34, 44, 90, 10, 8]
liste_triee = my_sort(ma_liste.copy())  


print("Liste triée :", liste_triee)