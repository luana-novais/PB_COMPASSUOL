import hashlib

while True:
    string = input("Digite uma string: ")

    hash = hashlib.sha1(string.encode())

    hash_hex = hash.hexdigest()

    print(f"O hash SHA-1 da string '{string}' é: {hash_hex}")
