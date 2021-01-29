import os
import struct
import hashlib
import sys

entropy = os.urandom(16)

string_bit = bin(int.from_bytes(entropy, byteorder=sys.byteorder))

print("Entropie: ", bin(int.from_bytes(entropy, byteorder=sys.byteorder))[2:])

m = hashlib.sha256(entropy).digest()
quatre_bits_string = bin(int.from_bytes(m, byteorder=sys.byteorder))[2:6]
entropy_string = bin(int.from_bytes(entropy, byteorder=sys.byteorder))

combined_bits = (entropy_string+quatre_bits_string)[2:]

print("Quatre premiers bits du SHA256 de l'entropie: ",quatre_bits_string)
print("Combinaison des deux: ",combined_bits)

split_combined_bits = []
for i in range(12):
    split_combined_bits.append(combined_bits[i*11:11*i+11])

print("Division en séries de 11 bits:",split_combined_bits)

bip_file = open("./english.txt",'r')
data = bip_file.read()
data = data.split('\n')

print("Les douzes mots selon la liste BIP39:")
seed = []
for e in split_combined_bits:
    word = data[int(e, 2)]
    print(word)
    seed.append(word)

def import_seed(list_words):
    res = []
    for word in list_words:
        res.append(bin(data.index(word))[2:])
    return res
     
print(import_seed(seed))