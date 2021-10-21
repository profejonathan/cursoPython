# Sistema de menú de un cajero (ATM)
print(
"""
    1. Extración
    2. Consultas
    3. Depositos
    4. Cambio de claves
    5. Salir
"""
)

opcion = int( input("Ingrese una opción: ") )
if opcion == 1: # Si es uno
    print("Menú de extraccion")
elif opcion == 2: # De lo contrario si
    print("Menú de consultas")
elif opcion == 3: # De lo contrario si
    print("Menú de depositos")
elif opcion == 4: # De lo contrario si
    print("Menú de cambios claves")
else:
    print("Opción invalida")