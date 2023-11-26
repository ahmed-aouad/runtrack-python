# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.


# len

def Taille(a):
    total=0
    for i in a:
        total+=1
    return total
# minimum
def mini(a):
    Min,cpt=a[0],0
    R=0
    for i in a: 
        cpt=cpt+1
        if i < Min:
            Min=i
            R=cpt-1
           # print(rg)
    return Min, R
# programme
New_liste=[]
t=[3, 1, 0, 45, 8, 9, 7]

# mini(t)
# taille(t)
# mini(t)
# print(mini(t))

for i in range(Taille(t)):
    print("lol")
    Min, R=mini(t)
    print(Min)
    New_liste.append(Min)
    print(R)
    t.pop(R)
    #t.remove(rg)
    print(t)
    print(New_liste)
   
    
    












# for i in a:
#     if i>(a[1]):
#         a.append(a[1])
#         del a[1]
#     else:
#         a.append(a[0])
#         del a[0]
#     print(i)

# L = [10,8,1,2]
# def trie(L):
#     print(1)
#     for i in taille(L):
#         temporaire=L[i]
#         j = i - 1
#         print(i)
#         while j >=0 and L[j] > temporaire:
#             L[j+1] = L[j]
#             j -= 1
#         L[j+1] = temporaire
#     return print(L)



            





