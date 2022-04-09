import requests

req = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
rsl = req.json()['ciphertext']

endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + rsl
dec = requests.get(endpointdec)
rsl1 = dec.json()['plaintext']

by = bytes.fromhex(rsl1)
finalrsl = by.decode()
print(finalrsl)