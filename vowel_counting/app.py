vowels = ['a', 'e', 'i', 'o', 'u']

word = str(input("Palavra: ")).lower()

#Lê-se: para cada item v dentro da lista vowels.
for v in vowels:
    print(f"{v}: {word.count(v)}")