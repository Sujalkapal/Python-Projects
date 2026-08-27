import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {key}")

#Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(cipher_text)

#Decrypt
plain_text = ""
cipher_text = input("Enter a message to decrypt: ")

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(plain_text) 