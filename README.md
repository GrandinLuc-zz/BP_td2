# Blockchain Programmation td2
Luc GRANDIN, Laith EL MERSHATI, Guillaume RICHER

## **BIP 0039**

### Création du programme 
Après la création du repo Github, nous avons décidé de créer le programme en python pour faire ce TD.
Le programme peut être éxecuter uniquement en lignes de commandes et seules sont néscéssaires les librairies :
* haslib 
* sys
* binascii
* escpy

### Création d'un entier aléatoire
Pour créer notre entier aléatoire (entropy) nous avons utilisé la fonction os.urandom de python qui est cryptographiquement sécurisée. Cet entier fait 128 bit, soit 16 bytes.

### Représentation de la seed en binaire 
Pour ce faire, nous avons hashé notre entier aléatoire préalablement calculé, puis converti ce hash en nombre binaire afin d'en extraire les 4 premier bit. 4 bits que nous avons concaténé à notre entropie créé précédement ainsi que convertit en nombre binaire.
Nous avons utilisé la fonction "bin" pour convertir les bytes en nombre binaires.
Nous avons systématiquement retiré les "0b" présents a chaque début de chaine binaire.

### Attribution à chaque lot d'un mot de la liste Bip 39
Pour faciliter l'attribution de chaque mot à chaque segment de 11 bits, nous avons stocké ces mêmes segments dans un liste de longueur 12.
Puis, à partir du fichier texte english.txt, présent sur la page GitHub du bip 39, nous attribuons à chaque segment de 11 bit le mot correspondant. A savoir que chacun des mot correspond a un unique segment de 11 bits, segments qui est égal au numéro de ligne du mot en question.

### Importation d'une seed mnemonic
Ce point est traité dans le script : "TD2_BIP39_import_seed.py"
Le procèdé pour l'importation d'une seed mnémonic est semblable au point précédent. Pour chacun des mots entrer par l'utilisateur dans la liste de la seed, nous convertissons le numéro de la ligne du mots correspondant en un nombre binaire de 11 bit que nous insérons dans la liste.
Il est important de souligner qu'il faut rajouter des 0 en debut de nombre binaire lorsqu'il ne font pas 11 bit de long, ce qui est souvent le cas.

## **BIP 0032**

