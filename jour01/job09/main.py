nom = "usb"
prix_unitaire = 15
quantité_en_stock = 135
print (nom)
print (prix_unitaire)
print (quantité_en_stock)

quantité_utilisateur = int(input("Quelle quantité souhaitez vous acheter?"))
# quantité_utilisateur <= quantité_en_stock
# quantité_en_stock = quantité_en_stock - quantité_utilisateur
quantité_en_stock -= quantité_utilisateur
# print(quantité_en_stock)
prix_unitaire *= 1.1
print(nom)
print(prix_unitaire)
print (quantité_en_stock)
# print (f" stock restant : {stock_apres_achat}")
# print (prix_unitaire)