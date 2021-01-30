import hashlib
import binascii
import sys

bip_0039 = open("english.txt",'r')
words = bip_0039.read()
words = words.split('\n')


example_seed = ['open', 'curious', 'climb', 'clog', 'strong', 'ridge', 'brush', 'capable', 'music', 'noodle', 'degree', 'jungle']
print("Exemple de seed : ", example_seed)

def import_seed(list_words):
    res = []
    for word in list_words:
        res.append(bin(words.index(word))[2:])
    return res

print("--------------------")     
print("Seed recuperee depuis l'example : ",import_seed(example_seed))

### Master private key ###

#il faut utiliser haslib sha512 pour hasher notre seed
#il faut caluculer la public key de notre private key, soit avec une librairie externe soit en utilisant le schema de dérivation des clés enfants renforcée

root_seed_list = import_seed(example_seed)
# PB : tout les éléments de la seed ne font pas tous 11 bits de long
# solution : on ajoute des 0 en debut de chaine pour que tout éléments de la seed fassent 11 bit de long

root_seed = ''
for elem in root_seed_list:
    if len(elem) != 11:
        while len(elem) < 11:
            elem = ('0'+elem) # Tout les éléments font 11 bit de long
    root_seed += elem
    
# la rout seed fait 132 bit de long, il faut y soustraire la checksum ( 4 dernier bit de la str )

root_seed = root_seed[:-4] # on retire les 4 dernier bit

print("--------------------")  
print("Root seed en binaire : ", root_seed)
print("--------------------")  
print("La longueur de la root seed est de : ",len(root_seed)) 

# transformation de la seed binaire en hexadecimal 
hexstr = "{0:0>4X}".format(int(root_seed,2)) 
data = binascii.a2b_hex(hexstr) 
print(type(data))
# Utilisation de haslib sur l'hexadecimal
output = hashlib.sha512(data).hexdigest()
output = output.encode('utf-8') # le hash de la seed ne semble pas être le bon

print("--------------------") 
print("Hash de la root seed : ",output)
print(type(output))

hash_root_bit = bin(int.from_bytes(output, byteorder=sys.byteorder))
hash_root_bit = hash_root_bit[2:]
print("--------------------") 
print(" Hash de la root seed sous forme binaire : ", hash_root_bit)
print(len(hash_root_bit)) # le hash est trop long pour être correct

### Master public key ###