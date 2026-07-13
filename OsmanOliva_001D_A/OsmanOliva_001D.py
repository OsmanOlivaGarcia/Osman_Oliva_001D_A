from os import system
system ("cls")

"""Poner en orden alfabetico"""


juegos = {}
inventario = {}


def leer_opcion():
    while True:
        try:
            menu = int(input())
            if menu > 6 or menu < 1:
                print("Opcion ingresada no valida")
            else:
                break
        except ValueError:
            print("Opcion ingresada no valida")
    return menu


def stock_plataforma(plataforma:str,juegos:dict,inventario:dict):
    totalStock = 0
    for i in juegos:
        juego = juegos[i][1]
        if juego.upper() == plataforma:
            totalStock += inventario[i][1]
    
    print(f"El total de stock disponible es: {totalStock}")


def busqueda_precio(p_min: int, p_max: int, juegos:dict, inventario:dict):
    listajuegos = []
    if p_min >= 0 and p_max > p_min:
        for i in juegos:
            if inventario[i][0] >= p_min and inventario[i][0] <= p_max:
                listajuegos.append(f"{juegos[i][0]}--{i}")
        if len(listajuegos) == 0:
            print("No hay juegos en ese rango de precios.")
        else:
            listajuegos.sort()
            print(listajuegos)

def buscar_codigo(codigo:str,juegos:dict,inventario:dict):
    if codigo in juegos:
        return True
    else:
        return False


def actualizar_precio(codigo:str, nuevo_precio:int,juegos:dict,inventario:dict):
            if buscar_codigo(codigo,juegos,inventario) == False:
                return False
            else:
                inventario[codigo][0] = nuevo_precio
                return True

def agregar_juego(codigo:str,titulo:str,plataforma:str,genero:str,clasificacion:str,multiplayer:str,editor:str,precio:str,stock:str,juegos:dict,inventario:dict):
    if codigo in juegos:
        return False
    else:
        precio = int(precio)
        stock = int(stock)
        juegos[codigo] = [titulo,plataforma,genero,clasificacion,multiplayer,editor]
        inventario[codigo] = [precio,stock]
        return True

def eliminar_juego(codigo:str,juegos:dict,inventario:dict):
    if buscar_codigo(codigo,juegos,inventario) == True:
        del juegos[codigo]
        del inventario[codigo]
        return True
    else:
        return False

"""Validaciones"""
def validacionCodigo(codigo:str,juegos:dict,inventario:dict):
    if codigo.strip() == "" and codigo not in juegos:
        return False
    else:
        True

def validacionTitulo(titulo:str):
    if titulo.strip() == "":
        return False
    else:
        return True
def validacionPlataforma(plataforma:str):
    if plataforma.strip() == "":
        return False
    else:
        return True

def validacionGenero(genero:str):
    if genero.strip() == "":
        return False
    else:
        return True

def validacionClasificacion(clasificacion:str):
    if clasificacion not in ("E","T","M"):
        return False
    else:
        return True

def validacionMultiplayer(multiplayer:str):
    if multiplayer not in ("S","N"):
        return False
    else:
        return True

def validacionEditor(editor:str):
    if editor.strip() == "":
        return False
    else:
        return True

def validacionPrecio(precio:str):
    try:
        precio = int(precio)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validacionStock(stock:str):
    try:
        stock = int(stock)
        if stock > 0:
            return True
        else:
            return False
    except ValueError:
        return False



"""--------------Menu-------------"""
while True:
    print("""==========MENÚ PRINCIPAL==========
1. Stock por plataforma
2. Búsqueda de juegos por de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
==============================""")
    menu = leer_opcion()
    
    if menu == 1:
        plataforma = input("Ingrese plataforma a consultar: ").upper()
        stock_plataforma(plataforma,juegos,inventario)
    elif menu == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
                
                
        while True:
            try:
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        
        busqueda_precio(p_min,p_max,juegos,inventario)
                
    elif menu == 3:
        while True:
            codigo = input("Ingrese el código del juego: ").upper()
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Valor ingresado no valido")
            actualizar_precio(codigo,nuevo_precio,juegos,inventario)
            if actualizar_precio(codigo,nuevo_precio,juegos,inventario) == True:
                print("Precio actualizado")
            else:
                print("El codigo no existe")
            while True:
                pregunta = input("¿Desea actualizar otro precio (s/n)?: ").upper()
                if pregunta not in ("S","N"):
                    print("Opcion ingresada no valida")
                else:
                    break
            if pregunta == "N":
                break

    elif menu == 4:
        codigo = input("Ingrese código del juego: ").upper()
        titulo = input("Ingrese título: ")
        plataforma = input("Ingrese plataforma: ")
        Genero = input("Ingrese género: ")
        clasificacion = input("Ingrese clasificación: ").upper()
        multiplayer = input("¿Es multiplayer?(s/n): ").upper()
        editor = input("Ingrese editor: ")
        precio = input("Ingrese precio: ")
        stock = input("Ingrese stock: ")
        
        if validacionCodigo(codigo,juegos,inventario) == False:
            print("El codigo ingresado no es valido")
        elif validacionTitulo(titulo) == False:
            print("El titulo ingresado no es valido")
        elif validacionPlataforma(plataforma) == False:
            print("La plataforma ingresada no es valida")
        elif validacionGenero(Genero) == False:
            print("El genero ingresado no es valido")
        elif validacionClasificacion(clasificacion) == False:
            print("La clasificacion ingresada no es valida")
        elif validacionMultiplayer(multiplayer) == False:
            print("La opcion ingresada no es valida:")
        elif validacionEditor(editor) == False:
            print("El editor ingresado no es valido")
        elif validacionPrecio(precio) == False:
            print("El precio ingresado no es valido")
        elif validacionStock(stock) == False:
            print("El stock ingresado no es valido")
        else:
            if agregar_juego(codigo,titulo,plataforma,Genero,clasificacion,multiplayer,editor,precio,stock,juegos,inventario) == True:
                print("Juego agregado")
            else:
                print("El codigo ya existe")
        
    elif menu == 5:
        codigo = input("Ingrese el codigo del juego que desea eliminar: ").upper()
        if eliminar_juego(codigo,juegos,inventario) == True:
            print("Juego eliminado")
        else:
            print("El codigo no existe")
        
    elif menu == 6:
        print("Programa finalizado")
        break