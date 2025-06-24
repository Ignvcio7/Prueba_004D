data = {"entradas": []}

def buscar_comprador(nombre_comprador: str):
    for comprador in data["entradas"]:
        if comprador["nombre_comprador"].lower() == nombre_comprador.lower():
            print("Comprador encontrado:", comprador)
            return comprador
    print("Comprador no encontrado")
    return None

def validar_nombre():
    while True:
        try:
            nombre_comprador = input("Ingrese nombre de comprador: ").strip()
            if not nombre_comprador.isalpha():
                print("El nombre solo debe contener letras.")
                continue
            
            for i in data["entradas"]:
                if i["nombre_comprador"].lower() == nombre_comprador.lower():
                    print("Nombre ya existe, intente con otro.")
                    continue
            return nombre_comprador
        except Exception:
            print("Ingrese un argumento válido")

def validar_categoria_entrada():
    while True:
        categoria = input("Ingrese categoría de entrada (G para General, V para VIP): ").strip().upper()
        if categoria not in ["G", "V"]:
            print("Debe ingresar G o V.")
            continue
        return categoria
    
def validar_letras_codigo_confirmacion(codigo: str):
    letra = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    for i in codigo:
        if i in letra:
            return True
    return False

def validar_numeros_codigo_confirmacion(codigo: str):
    numeros = "1234567890"
    for i in codigo:
        if i in numeros:
            return True
    return False        

def validar_codigo_confirmacion():
    while True:
        try:
            codigo = input("Ingrese el codigo de confirmacion: ")
            if validar_numeros_codigo_confirmacion(codigo) and validar_letras_codigo_confirmacion(codigo):
                if len(codigo) >= 6:
                    print("Código creado con éxito!")
                    return codigo
                else:
                    print("El código debe tener al menos 6 caracteres.")
                    continue
            else:
                print("El código de confirmación debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacios en blanco.")
                continue
        except ValueError:
            print("Solo ingrese caracteres válidos")

def validar_numero_entero_positivo(mensaje_input: str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero < 0:
                print("Debe ingresar un número positivo.")
                continue
            return numero
        except ValueError:
            print("Solo puede ingresar números enteros")

def agregar_comprador():
    while True:
        nombre = validar_nombre()
        if nombre is None:
            continue
        categoria = validar_categoria_entrada()
        codigo = validar_codigo_confirmacion()
        comprador = {
            "nombre_comprador": nombre,
            "categoria_entrada": categoria,
            "codigo_comprador": codigo
        }
        data["entradas"].append(comprador)
        print("¡Comprador agregado exitosamente!")
        break

def cancelar_compra():
    nombre = input("Ingrese el nombre del comprador a cancelar: ").strip()
    for i, comprador in enumerate(data["entradas"]):
        if comprador["nombre_comprador"].lower() == nombre.lower():
            del data["entradas"][i]
            print("Compra cancelada con éxito.")
            return
    print("No se encontró un comprador con ese nombre.")

def menu():
    while True:
        print("--- MENU COMPRA DE ENTRADAS 'EL CONEJO BUENO' ---")
        print("[1] --- COMPRAR ENTRADAS ---")
        print("[2] --- CONSULTAR COMPRADOR ---")
        print("[3] --- CANCELAR COMPRA ---")
        print("[4] --- SALIR ---")

        try:
            opcion = validar_numero_entero_positivo("Seleccione una opción: ")
            if opcion < 1 or opcion > 4:
                print("La opción ingresada no existe, intente de nuevo.")
                continue
        except ValueError:
            print("Ingrese un número válido")

        if opcion == 1:
            print("--- COMPRANDO ENTRADA ---")
            agregar_comprador()
             
        elif opcion == 2:
            print("--- BUSCANDO COMPRADOR ---")
            nombre = input("Ingrese el nombre del comprador: ").strip()
            buscar_comprador(nombre)

        elif opcion == 3:
            print("--- ELIMINAR COMPRADOR ---")
            cancelar_compra()

        elif opcion == 4:
            print("Saliendo...")
            break

menu()