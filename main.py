#Menu Principal
from funciones import suma,resta,multi,div
while True:
    """
    1)Suma  
    2)Resta
    3)Multiplicacion
    4)Division
    5)Salir
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

    elif opcion == 3:
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese EL segundo numero "))
        multi (num1, num2)

    elif opcion == 4:
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese EL segundo numero "))
        div (num1, num2)
