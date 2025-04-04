#Menu Principal
from funciones import suma,resta
while True:
    """
    1)suma  
    2)resta
    3)
    4)
    5) Salir
    """
    opcion = int(input("Seleccione su opcion: "))
    if opcion == 1:
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese EL segundo numero "))
        suma (num1, num2)
    elif opcion == 2:
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese EL segundo numero "))
        resta (num1, num2)
