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
    pw_dict = {
        'password': pw_tup[0],
        'key': pw_tup[1]
    }
    json_str = json.dumps(pw_dict)
    return json_str


def decrypt(cipher_json):
    data = json.loads(cipher_json)
    ciphered_pw = data['password']
    key = data['key']

    decrypt_pw = ""
    for character in ciphered_pw:
        index = key.index(character)
        decrypt_pw += chars[index]
    return decrypt_pw


test_one = 'HelloWorld'
print(test_one)
pw_encrypt = encrypt(test_one)
print(pw_encrypt)
print(decrypt(pw_encrypt))
