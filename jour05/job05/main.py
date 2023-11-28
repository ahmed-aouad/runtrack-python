
def chiffrement_cesar(message, decalage):
    message_chiffre = ""


    for char in message:
        if char.isalpha():
            # Vérifier si le caractère est une lettre
            majuscule = char.isupper()
            char_code = ord(char.upper())
            char_code_decale = (char_code - ord('A') + decalage) % 26 + ord('A')
            char_chiffre = chr(char_code_decale)
            if not majuscule:
                char_chiffre = char_chiffre.lower()
            message_chiffre += char_chiffre
        else:
            # Conserver les caractères non alphabétiques inchangés
            message_chiffre += char


    return message_chiffre


# Exemple d'utilisation
message_original = "Veni, vidi, vici"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")