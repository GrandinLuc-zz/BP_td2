# Blockchain Programmation td2
Luc GRANDIN, Laith EL MERSHATI, Guillaume RICHER

## Instruction 
Après la création du repo Github, nous avons décidé de créer le programme en python pour faire ce TD.
Le programme peut être exécuté uniquement en lignes de commandes et seules sont néscessaires les librairies :
* hashlib 
* binascii
* hmac
* escpy

Pour lancer la première partie du TD depuis la console 
* python .\TD_BIP39.py
pour la dernière question de la première partie du TD
* python .\TD2_BIP39_import_seed.py 

Pour lancer la seconde partie du TD depuis la console 
* python .\TD_BIP32.py

## **BIP 0039**

### Création d'un entier aléatoire
Pour créer notre entier aléatoire (entropy) nous avons utilisé la fonction os.urandom de python qui est cryptographiquement sécurisée. Cet entier fait 128 bit, soit 16 bytes.

### Représentation de la seed en binaire 
Pour ce faire, nous avons hashé notre entier aléatoire préalablement calculé, puis converti ce hash en nombre binaire afin d'en extraire les 4 premier bit. Nous les avons ensuite concaténé à notre entropie créée précédement et nous avons convertit le tout en nombre binaire.
Nous avons utilisé la fonction "bin" pour convertir les bytes en nombre binaires.
Nous avons systématiquement retiré les "0b" présents a chaque début de chaine binaire.

### Attribution à chaque lot d'un mot de la liste Bip 39
Pour faciliter l'attribution de chaque mot à chaque segment de 11 bits, nous avons stocké ces mêmes segments dans un liste de longueur 12.
Puis, à partir du fichier texte english.txt, présent sur la page GitHub du bip 39, nous attribuons à chaque segment de 11 bit le mot correspondant. A savoir que chacuns des mots correspond à un unique segment de 11 bits, segment qui est égal au numéro de ligne du mot en question.

### Importation d'une seed mnemonic
Ce point est traité dans le script : "TD2_BIP39_import_seed.py"
Le procédé pour l'importation d'une seed mnémonic est semblable au point précédent. Pour chacun des mots entrés par l'utilisateur dans la liste de la seed, nous convertissons le numéro de la ligne du mots correspondant en un nombre binaire de 11 bit que nous insérons dans la liste.
Il est important de souligner qu'il faut rajouter des 0 en début de nombre binaire lorsqu'il ne font pas 11 bit de long, ce qui est souvent le cas.

## **BIP 0032**

### Extraction de la master private key et du chain code
Dans cette partie nous utilisons un mnemonic exemple : ['open', 'curious', 'climb', 'dog', 'strong', 'ridge', 'brush', 'capable', 'music', 'noodle', 'degree', 'jungle']. A cette seed nous appliquons la fonction d'importation de seed afin de travailler sur notre seed en binaire.
Cette seed est ensuite convertie en hexadecimal, afin d'être hashé avec la fonction sha512 de la librairie hashlib. Finalement nous obtenons un hash, qui une fois converti en nombre binaire fait 512 bit de long et ainsi, les 256 premier bit forment la "master private key" et 256 bit suivant forment le "master chain code".
