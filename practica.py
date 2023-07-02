from cliente import Cliente
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
# CRUD CLIENTE

data_clientes:list= [{"numero_documento":"76015974",
                     "razon_social":"Juan Anderson Coasaca Huanca",
                     "direccion":"Jr. Pumacahua 932",
                     "telefono":"901158525"},
                     {"numero_documento":"72198998",
                     "razon_social":"Moises Joaquin Mestas Maque",
                     "direccion":"Jr. Lampa 756",
                     "telefono":"965645314"},
                     {"numero_documento":"75614685",
                     "razon_social":"Jose Manuel Quispe Condori",
                     "direccion":"Arequipa - Cerro Colorado",
                     "telefono":"902962848"},
                     {"numero_documento":"74027874",
                     "razon_social":"Julmer Puma Condori ",
                     "direccion":"OVALO SALIDA AREQUIPA",
                     "telefono":" 931939784"}]

clientes:Cliente = []

def cargar_datos_clientes():
    for data in data_clientes:
        clientes.append(Cliente(data["numero_documento"],
                                data["razon_social"],
                                data["direccion"],
                                data["telefono"]))
    return clientes

def insertar_cliente():
    numero_documento:str=input("Ingrese el numero de docuemto del cliente: ")
    razon_social:str=input("Ingrese la razon social del cliente: ")
    direccion:str=input("Ingrese la direccion del cliente: ")
    telefono:str=input("Ingrese telefono del cliente: ")
    clientes.append(Cliente(numero_documento,razon_social,direccion,telefono))
    return clientes

def listar_clientes():
    for cliente in clientes:
        print(cliente.convertir_a_texto())
    return clientes

def buscar_cliente():
    numero_documento:str=input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            return cliente

def editar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento para editar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            cliente.razon_social=input("Ingrese nueva razon social del cliente: ")
            cliente.direccion=input("Ingrese nueva direcion del cliente: ")
            cliente.telefono=input("Ingrese nuevo telefono del cliente: ")
    listar_clientes()
    return clientes

def eliminar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento del cliente para eliminar: ")
    for indice, cliente in enumerate(clientes):
        if cliente.numero_documento==numero_documento:
            clientes.pop(indice)
    listar_clientes()   
    return clientes

# CRUD PRODUCTO

data_productos:list=[
                      {"Codigo":"T1",
                     "Nombre":"MSI GEFORCE RTX 4060 Ti 8GB ",
                     "Precio":2100.00},
                     {"Codigo":"T2",
                     "Nombre":"Tarjeta Gráfica NVIDIA GeForce RTX 4090",
                     "Precio":4500.00},
                     {"Codigo":"P1",
                     "Nombre":"PROCESADOR INTEL CORE I9 10900F 2.80GHZ",
                     "Precio": 3200.00},
                     {"Codigo":"P2",
                     "Nombre":"Procesador Intel® Core™ i5-1135G7",
                     "Precio":1700.00},
                     {"Codigo":"M1",
                     "Nombre":"MEMORIA RAM KINGSTON FURY RENEGADE RGB 8GB DDR4 3200MHZ",
                     "Precio":195.00},
                     {"Codigo":"M2",
                     "Nombre":"MEMORIA RAM TG T-FORCE DELTA RGB WHITE, 8GB, DDR4 3200 MHZ",
                     "Precio":150.00},
                     {"Codigo":"R1",
                     "Nombre":"REFRIGERACION LIQUIDA CORSAIR HYDRO SERIES H100i RGB",
                     "Precio":660.00},
                     {"Codigo":"R2",
                     "Nombre":"REFRIGERACION LIQUIDA DEEPCOOL GAMMAXX L240 A-RGB, WH",
                     "Precio":334.00},
                     {"Codigo":"SSD1",
                     "Nombre":"Ssd Kingston 1TB Nv2 Pcie 4.0 Nvme M.2 ",
                     "Precio":227.00},
                      {"Codigo":"SSD2",
                     "Nombre":"Ssd Samsung 970 EVO Plus MZ-V7S1T0B/AM 1TB ",
                     "Precio":310.00},
                     {"Codigo":"CA1",
                     "Nombre":"CASE MSI MAG FORGE M100A USB 3.2 GEN 1 TYPE-A AUTO-RGB",
                     "Precio":170.00},
                      {"Codigo":"CA2",
                     "Nombre":"CASE CORSAIR 7000D AIRFLOW BLACK TEMPERED GLASS FULL",
                     "Precio":650.00},
                     {"Codigo":"F1",
                     "Nombre":"FUENTE DE PODER GAMBYTE GN600 ATX, BASIC OEM NO MODULAR,",
                     "Precio":110.00},
                      {"Codigo":"F2",
                     "Nombre":"FUENTE DE PODER COOLER MASTER 750W ATX, BRONZE 80 PLUS",
                     "Precio":350.00},
                     {"Codigo":"M1",
                     "Nombre":"MOUSE LOGITECH G G305 LIGHTSPEED WIRELESS GAMING USB BLACK",
                     "Precio":350.00},
                     {"Codigo":"M2",
                     "Nombre":"MOUSE GENIUS DX-110 NEGRO",
                     "Precio":15.00},
                      {"Codigo":"TE1",
                     "Nombre":"TECLADO MECANICO INALAMBRICO LOGITECH G915 LIGHTSPEED RGB",
                     "Precio":770.00},
                      {"Codigo":"TE2",
                     "Nombre":"TECLADO CYBERTEL GAMER MECANICO EXPLORER",
                     "Precio":75.00},
                     {"Codigo":"TE3",
                     "Nombre":"Teclado gamer Redragon Kumara K552 QWERTY Outemu Red español latinoamérica color negro con luz RGB",
                     "Precio":75.00},
                     {"Codigo":"MON1",
                     "Nombre":"Monitor Gamer LG UltraGear 23.8'' IPS 144Hz 1ms FreeSync Premium 24GN60R",
                     "Precio":839.00},
                     {"Codigo":"MON2",
                     "Nombre":"Monitor AOC 19.5'' HD E2070SWHN",
                     "Precio":250.00},]

productos:Producto = []
def cargar_datos_productos():
    for data in data_productos:
        productos.append(Producto(data["Codigo"],
                                data["Nombre"],
                                data["Precio"]))
    return productos

def insertar_producto():
    codigo:str=input("Ingrese codigo del producto: ")
    nombre:str=input("Ingrese nombre del producto: ")
    precio:str=input("Ingrese precio del producto: ")
    productos.append(Producto(codigo,nombre,precio))
    return productos

def listar_productos():
    for producto in productos:
        print(producto.convertir_a_texto())
    return productos

def buscar_producto():
    codigo:str=input("Ingrese codigo del producto para buscar producto: ")
    codigo=codigo.upper()
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            return producto
    if producto.codigo!=codigo:
        print("Producto no registrado o codigo digitado")
        buscar_producto()
        return producto

def editar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para editar producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            producto.nombre=input("Ingrese nuevo nombre del producto: ")
            producto.precio=float(input("Ingrese nuevo precio del producto: "))
           
    listar_productos()
    return productos

def eliminar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para eliminar producto: ")
    for indice, producto in enumerate(productos):
        if producto.codigo==codigo:
            productos.pop(indice)
    listar_productos()
    return productos
   

# CRUD VENTA
ventas:Venta=[]
venta_detalles:VentaDetalle=[]
def agregar_productos():
    producto:Producto=buscar_producto()
    cantidad:float=float(input("Ingrese la cantidad del producto: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,
                                       producto.codigo,
                                       producto.nombre,
                                       cantidad,
                                       producto.precio))
    return venta_detalles


def insertar_venta():
    cliente:Cliente=buscar_cliente()
    continuar_venta:bool=True
    while continuar_venta:
        opcion:str=input("1: para agregar producto, 2 para guargar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_venta=False
    total:float=0
    for venta_detalle in venta_detalles:
        total=total+venta_detalle.total
    ventas.append(Venta(len(ventas)+1,cliente,venta_detalles,total))
    return ventas
def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
    return ventas
        
def buscar_venta():
    numero:int=int(input("Ingrese el numero de la venta para bucar: "))
    for venta in ventas:
        if venta.numero==numero:
            print("\n|════════════════════════ BOLETA DE VENTA ════════════════════════════| \n       ▂ ▃ ▄ ▅ ▆ ▇ █ █  𝐈 𝐍 𝐍 𝐎 𝐕 𝐀 - 𝓟 𝓒  𝐒.𝐀.𝐂.  █ █ ▇ ▆ ▅ ▄ ▃ ▂")
            print("\n================================")
            print(venta.convertir_a_texto())
            print("================================")
            for venta_detalle in venta.detalle:
                print(venta_detalle.convertir_a_texto())
                print("================================")
            return venta 

def mostrar_tienda_fisica():
    print("░░░░░░░░░░░░░░░░░░░░【  𝐈 𝐍 𝐅 𝐎 𝐑 𝐌 𝐀 𝐂 𝐈 𝐎 𝐍 - 𝐃 𝐄 - 𝐋 𝐀 - 𝐓 𝐈 𝐄 𝐍 𝐃 𝐀 】░░░░░░░░░░░░░░░░░░░░\n")
    print("Tienda Física: INNOVA -- PC -- S.A.C".center(90))
    print("Dirección: Jr. Manuel Gonzales Prada N°501, Galería-KUSKA".center(90))
    print("✆Teléfono: 951685936".center(90))
    print("Horario: Lunes a Viernes de 9:00 AM a 6:00 PM\n".center(90))
    
def menu_texto():
    print("\n       ▂ ▃ ▄ ▅ ▆ ▇ █ █  𝐈 𝐍 𝐍 𝐎 𝐕 𝐀 - 𝓟 𝓒  𝐒.𝐀.𝐂.  █ █ ▇ ▆ ▅ ▄ ▃ ▂ ")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰  MENU DE OPCIONES  ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ ")
    print("░░░░░░░░░░░░░░░░░░░░【  𝙈 𝙀 𝙉 𝙐 - 𝘾 𝙇 𝙄 𝙀 𝙉 𝙏 𝙀  】░░░░░░░░░░░░░░░░░░░░\n")
    print(" ⫸  OPCIÓN 0: Mostrar tienda física")
    print(" ⫸  OPCIÓN 1: Insertar Cliente")
    print(" ⫸  OPCIÓN 2: Listar Cliente")
    print(" ⫸  OPCIÓN 3: Buscar Cliente")
    print(" ⫸  OPCIÓN 4: Editar Cliente")
    print(" ⫸  OPCIÓN 5: Elimiar Cliente\n")
    print("░░░░░░░░░░░░░░░░░░░░【  𝙈 𝙀 𝙉 𝙐 - 𝙋 𝙍 𝙊 𝘿 𝙐 𝘾 𝙏 𝙊 】░░░░░░░░░░░░░░░░░░░\n")
    print(" ⫸  OPCIÓN 6: Insertar Producto")
    print(" ⫸  OPCIÓN 7: Listar Producto")
    print(" ⫸  OPCIÓN 8: Buscar unProducto")
    print(" ⫸  OPCIÓN 9: Editar Producto")
    print(" ⫸  OPCIÓN 10: Elimiar Producto\n")  
    print("░░░░░░░░░░░░░░░░░░░░░【  𝙈 𝙀 𝙉 𝙐 - 𝙑 𝙀 𝙉 𝙏 𝘼   】░░░░░░░░░░░░░░░░░░░░░░\n")
    print(" ⫸  OPCIÓN 11: Insertar Venta")
    print(" ⫸  OPCIÓN 12: Listar Venta")
    print(" ⫸  OPCIÓN 13: Buscar Venta")
    print(" ⫸  OPCIÓN 30: Finalizar Programa\n")
    
def menu():
    continuar:bool=True
    while continuar:
        menu_texto()
        opcion:str=input("Ingrese la opcion: ")
        match opcion:
            case "0":
                mostrar_tienda_fisica()
            case "1":
                insertar_cliente()
            case "2":
                listar_clientes()
            case "3":
                buscar_cliente() 
            case "4":
                editar_cliente()   
            case "5":
                eliminar_cliente() 
            case "6":
                insertar_producto()
            case "7":
                print("┌─────────────────────────────────── ⋅≪   𝐂 𝐀 𝐓 𝐀 𝐋 𝐎 𝐆 𝐎   𝐂 𝐎 𝐌 𝐄 𝐑 𝐂 𝐈 𝐀 𝐋   ≫⋅ ───────────────────────────────────┐ \n")
                listar_productos()
            case "8":
                buscar_producto() 
            case "9":
                editar_producto()   
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta() 
            case "30":
                continuar=False    

def main():
    cargar_datos_clientes()
    cargar_datos_productos()
    menu()
    print("FINALIZANDO PROGRAMA")
    return True
if __name__=='__main__':
    main()




