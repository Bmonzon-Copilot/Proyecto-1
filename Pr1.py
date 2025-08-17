##QUICK SORT POR NOMBRE
class Ordenador():
    def OrdenadorNombre(lista):
        try:
            if len(lista) <= 1:
                return lista
            pivote = lista[0].nombre
            menores = [x for x in lista[1:] if x.nombre < pivote]
            iguales = [x for x in lista if x.nombre == pivote]
            mayores = [x for x in lista[1:] if x.nombre > pivote]
            return Ordenador.OrdenadorNombre(menores) + iguales + Ordenador.OrdenadorNombre(mayores)
        except ValueError:
            print("NOTIFICACION: AUN NO HAY PRODUCTOS INGRESADOS...")

    def OrdenadorPrecio(lista):

         try:
             if len(lista) <= 1:
                 return lista
             pivote = lista[0].precio
             menores = [x for x in lista[1:] if x.precio<pivote]
             iguales = [x for x in lista if x.precio==pivote]
             mayores = [x for x in lista[1:]if x.precio>pivote]
             return Ordenador.OrdenadorPrecio(menores) + iguales + Ordenador.OrdenadorPrecio(mayores)
         except ValueError:
             print("NOTIFICACION: AUN NO HAY PRODUCTOS INGRESADOS...")


    def OrdenadorStock(lista):
        try:
            if len(lista) <= 1:
                return lista
            pivote = lista[0].stock
            menores = [x for x in lista[1:] if x.stock < pivote]
            iguales = [x for x in lista if x.stock == pivote]
            mayores = [x for x in lista[1:] if x.stock > pivote]
            return Ordenador.OrdenadorStock(menores) + iguales + Ordenador.OrdenadorStock(mayores)

        except ValueError:
            print("NOTIFICACION: AUN NO HAY PRODUCTOS INGRESADOS...")






from dis import code_info
class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_info_producto(self):
        return (f"Codigo: {self.codigo} - Nombre: {self.nombre} - Categoria: {self.categoria} - "
                f"Precio: {self.precio} - Stock: {self.stock}")

class RegistrarProducto:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self):
        while True:
            codigo = input("Ingrese código del Producto: ").strip()
            if not codigo:
                print("Error: El código no puede estar vacío.\n")
                continue
            if codigo in self.productos:
                print(f"Error: El código '{codigo}' ya está registrado.\n")
                continue
            break

        while True:
            nombre = input("Ingrese nombre del producto: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío.\n")
                continue
            break

        categorias_validas = ["Alimento", "Electronico", "Ropa", "Higiene"]
        while True:
            print("********* Categorías ********")
            for i, categ in enumerate(categorias_validas, start=1):
                print(f"{i}. {categ}")
            try:
                opcion = int(input("Seleccione una categoría (1-4): "))
                if 1 <= opcion <= len(categorias_validas):
                    categoria = categorias_validas[opcion - 1]
                    break
                else:
                    print("Error: Seleccione un número válido entre 1 y 4.\n")
            except ValueError:
                print("Error: Debe ingresar un número entero.\n")

        while True:
            try:
                precio = float(input("Ingrese Precio Q(0.0): "))
                if precio <= 0:
                    print("Error: El precio debe ser mayor a 0.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un valor numérico.\n")

        while True:
            try:
                stock = int(input("Ingrese Stock: "))
                if stock < 0:
                    print("Error: El stock no puede ser negativo.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número entero para el stock.\n")

        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos[codigo] = producto
        print("Producto ingresado exitosamente...\n")

    def mostrar_producto(self):
        if not self.productos:
            print("No existen productos registrados.\n")
            return
        for producto in self.productos.values():
            print(producto.mostrar_info_producto())


    def mostrarOrdenadosNm(self):
        if not self.productos:
            print("No existen productos registrados.\n")
            return
        lista = list(self.productos.values())
        ordenados = Ordenador.OrdenadorNombre(lista)
        print("Productos Ordenados: Nombre")
        for var in ordenados:
            print(var.mostrar_info_producto())

    def mostrarOrdenadosPr(self):
        if not self.productos:
            print("No existen productos registrados.\n")
            return
        lista = list(self.productos.values())
        ordenados = Ordenador.OrdenadorPrecio(lista)
        print("Productos Ordenados: Precio")
        for var1 in ordenados:
            print(var1.mostrar_info_producto())

    def mostrarOrdenadosSt(self):
        if not self.productos:
            print("No existen productos registrados.\n")
            return
        lista = list(self.productos.values())
        ordenados = Ordenador.OrdenadorStock(lista)
        print("Productos Ordenados: Stock")
        for var2 in ordenados:
            print(var2.mostrar_info_producto())

class ActulizarProducto:
    def __init__(self,registro):
        self.registro = registro
        self.categorias = ["Alimento", "Electronico", "Ropa", "Higiene"]

    def actualizacion(self):
        if not self.registro.productos:
            print("No hay productos registrados...")
            return

        while True:
            codigo = input("Ingrese codigo a actulizar: ").strip()
            if not codigo:
                print("Error. Ingrese un codigo.\n")
                continue
            if codigo not in self.registro.productos:
                print(f"Error. El producto con el codigo '{codigo}'no existe.\n")
                continue
            break

        info_actual = self.registro.productos[codigo] #p=info_actual
        print("Informacion Actual")
        print(info_actual.mostrar_info_producto())

        while True:
            nuevo_nombre = input(f"Nuevo nombre [{info_actual.nombre}]: ").strip()
            if nuevo_nombre == "":
                break
            if nuevo_nombre:
                info_actual.nombre = nuevo_nombre
                break
            print("Error: el nombre no puede estar vacío.\n")

        while True:




            print("\n********* Categorías ********")
            for i, categ in enumerate(self.registro.categorias, start=1):
                print(f"{i}. {categ}")
            opc = input(
                f"Seleccione la nueva categoría (1-{len(self.registro.categorias)}) "
                f"o Enter para mantener [{info_actual.categoria}]: "
            ).strip()
            if opc == "":
                break
            try:
                n = int(opc)
                if 1 <= n <= len(self.registro.categorias):
                    info_actual.categoria = self.registro.categorias[n - 1]
                    break
                else:
                    print(f"Error: número fuera de rango (1-{len(self.registro.categorias)}).\n")
            except ValueError:
                print("Error: debe ingresar un número entero.\n")

        while True:
            prec = input(f"Nuevo precio [{info_actual.precio}] Q(0.0): ").strip()
            if prec == "":
                break
            try:
                precio = float(prec)
                if precio > 0:
                    info_actual.precio = precio
                    break
                print("Error: el precio debe ser mayor que 0.\n")
            except ValueError:
                print("Error: ingrese un valor numérico para el precio.\n")

        while True:
            existencia = input(f"Nuevo stock [{info_actual.stock}]: ").strip()
            if existencia == "":
                break
            try:
                stock = int(existencia)
                if stock >= 0:
                    info_actual.stock = stock
                    break
                print("Error: el stock no puede ser negativo.\n")
            except ValueError:
                print("Error: ingrese un número entero para el stock.\n")

        print("\nProducto actualizado exitosamente...")
        print(info_actual.mostrar_info_producto())
        print()





def MenuOrdenador():
    print("---> OPCIONES DE ORDENAMIENTO <---")
    print("1. Ordenar por nombre")
    print("2. Ordenar por precio")
    print("3. Ordenar por stock")
    print("4. Regresar: ")
    print("Opcion a ingresar: ")

def MenuPrincipal():
    print("---> SMART STOCK <---")
    print("1. Registrar productos")
    print("2. Inventario")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("5. Ordenar productos")
    print("6. Salir")

opcionMenuP = 0
opcionMenuO = 0
registroProducto = RegistrarProducto()
actualizacion = ActulizarProducto(registroProducto)

while opcionMenuP != 6:
    MenuPrincipal()
    opcionMenuP = int(input("Opcion a ingresar: "))
    match(opcionMenuP):
        case 1:
            print("REGISTRO DE PRODUCTOS")
            registroProducto.agregar_producto()
        case 2:
            print("INVENTARIO DE PRODUCTOS")
            registroProducto.mostrar_producto()
        case 3:
            print("ACTUALIZAR PRODUCTOS")
            actualizacion.actualizacion()
        case 4:
            pass
        case 5:
            MenuOrdenador()
            opcionMenu0 = int(input("1. Opcion a ingresar: "))

            match(opcionMenu0):
                case 1:
                    print("ORDEN POR NOMBRE")
                    registroProducto.mostrarOrdenadosNm()
                case 2:
                    print("ORDEN POR PRECIO")
                    registroProducto.mostrarOrdenadosPr()
                case 3:
                    print("ORDEN POR STOCK")
                    registroProducto.mostrarOrdenadosSt()
                case 4:
                    print("REGRESANDO AL MENU")
                case _:
                    print("OPCION NO VALIDA")
        case 6:
            print("SALIENDO DEL SISTEMA. GRACIAS POR SU VISITA :)")
        case _:
            print("OPCION NO VALIDA")
