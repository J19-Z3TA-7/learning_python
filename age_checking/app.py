age = int(input("Type in your age: "))
if age < 15:
    print("Você ainda é muito novo.")
elif age <= 18:
    print("Você precisa crescer um pouco mais!")
elif age <= 30:
    print("O tempo passou rápido!")
elif age < 100:
    print("Está crescido...")
elif age < 400:
    print("Você é num vampiro?")
else:
    print("Viu o início de tudo?")