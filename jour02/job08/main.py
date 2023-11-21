a = int(input("longueur du côté 1"))
b = int(input("longueur du côté 2"))
c = int(input("longueur du côté 3"))


if a <= b + c and b <= a + c and c <= a + b:
    print("Triangle possible")
  # inégalité triangulaire 
else:
    print("Triangle impossible, changez les longueurs ")