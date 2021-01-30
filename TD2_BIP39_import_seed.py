split = []

with open('./english.txt', 'r') as reader:
    words = reader.read().split("\n")
    for i in range(12):
        word = input("Enter word {} : ".format(i+1))
        try:
            binary_index = bin(words.index(word))[2:]
            binary_index = '0'*(11-len(binary_index)) + binary_index
            split.append(binary_index)
        except:
            print("Word doesn't exit, please try again.")
            exit()

print()
print(split, end="\n\n")

entropy_checksum = ""
for i in split:
    entropy_checksum = entropy_checksum + i

print(entropy_checksum, end="\n\n")

print("Entropy :\n", entropy_checksum[:-4])
print()
print("Checksum :\n", entropy_checksum[-4:])