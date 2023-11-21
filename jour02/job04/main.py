N = input("entrée la valeur N: ")
 
print(f"voici la table de {N}:") 

for i in range (1,11):
    result=int(N) * int(i)

    print(f"{N}*{i}={result}")
   