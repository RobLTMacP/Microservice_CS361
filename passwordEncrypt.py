import random
import string
import json

chars = string.ascii_letters + string.digits + string.punctuation


def generate_key():
    key = list(chars)
    random.shuffle(key)
    return key


def encrypt(password):
    key = generate_key()
    cipher_pw = ""
    for character in password:
        index = chars.index(character)
        cipher_pw += key[index]
    pw_tup = (cipher_pw, key)
    json_str = json.dumps(pw_tup)
    return json_str


def decrypt(ciphered_pw, key):
    decrypt_pw = ""
    for character in ciphered_pw:
        index = key.index(character)
        decrypt_pw += chars[index]
    return decrypt_pw


test_one = 'HelloWorld'
pw_encrypt = encrypt(test_one)
print(pw_encrypt)




