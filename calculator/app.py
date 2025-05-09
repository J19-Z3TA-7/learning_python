n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
operation = int(input("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão"))

if operation == 1:
  print(n1+n2)
elif operation == 2:
  print(n1-n2)
elif operation == 3:
  print(n1*n2)
elif operation == 4:
  print(f"{n1/n2}\nResto: {n1%n2}")
else:
  print("Operação inválida.")

