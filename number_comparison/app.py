number1 = float(input("Primeiro número: "))
number2 = float(input("Segundo número: "))

if number1 > number2:
    print(f"O primeiro é maior: ({number1})")
elif number1 < number2:
    print(f"O segundo é maior: ({number2})")
else:
    print("São iguais.")