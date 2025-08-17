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
            codigo = input("Ingrese código del Producto: ").strip() #Ingreso de codigo
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

        categorias_validas = ["Alimento", "Electronico", "Ropa", "Higiene"] #lista con opciones de categorias
        while True:
            print("********* Categorías ********")
            for i, categ in enumerate(categorias_validas, start=1):
                print(f"{i}. {categ}")
            try:
                opcion = int(input("Seleccione una categoría (1-4): "))# Seleccion de categoria
                if 1 <= opcion <= len(categorias_validas):
                    categoria = categorias_validas[opcion - 1]
                    break
                else:
                    print("Error: Seleccione un número válido entre 1 y 4.\n")
            except ValueError:
                print("Error: Debe ingresar un número entero.\n")

        while True:
            try:
                precio = float(input("Ingrese Precio Q(0.0): ")) #Ingreso de Precio
                if precio <= 0:
                    print("Error: El precio debe ser mayor a 0.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un valor numérico.\n")

        while True:
            try:
                stock = int(input("Ingrese Stock: ")) #Ingreso de Stock
                if stock < 0:
                    print("Error: El stock no puede ser negativo.\n")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número entero para el stock.\n")

        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos[codigo] = producto
        print("Producto ingresado exitosamente...\n")

    def mostrar_producto(self): #Muestra informacion de nuestro diccionario
        if not self.productos:
            print("No existen productos registrados.\n")
            return
        for producto in self.productos.values():
            print(producto.mostrar_info_producto())

class ActualizarProducto:
    def __init__(self, registro):
        self.registro = registro

    def actualizacion(self):
        if not self.registro.productos:
            print("No hay productos registrados...\n")
            return

        while True:
            codigo = input("Ingrese código a actualizar: ").strip()
            if not codigo:
                print("Error. Ingrese un código.\n")
                continue
            if codigo not in self.registro.productos:
                print(f"Error. El producto con el código '{codigo}' no existe.\n")
                continue
            break

        info_actual = self.registro.productos[codigo]

        print("\n--- Información actual ---")
        print(info_actual.mostrar_info_producto())

        while True:
            nuevo_nombre = input(f"Nuevo nombre [{info_actual.nombre}] preciona enter para mantener: ").strip()
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

class EliminarProducto:
    def __init__(self,registro):
        self.registro = registro

    def eliminar(self):
        if not self.registro.productos:
            print("No hay productos registrados")
            return

        while True:
            codigo = input("Ingrese EL codigo del producto a eliminar: ").strip()
            if not codigo:
                print("Error,Debe de colocar un codigo")
                continue
            if codigo not in self.registro.productos:
                print(f"Error, el codigo ingresado '{codigo}' no pertenece a ningun producto.\n")
                continue
            break

        info_actual = self.registro.productos[codigo]
        print("/n-----Producto a Eliminar-----")
        print(info_actual.mostrar_info_producto())

        while True:
            confir = input("Quiere eliminar el producto (s/n): ").strip().lower()
            if confir == "s":
                del self.registro.productos[codigo]
                print("Producto eliminado correctamente...\n")
                break
            elif confir == "n":
                print("Operacion cancelada.\n")
                break
            else:
                print("Ingrese 's' o 'n'.\n")









