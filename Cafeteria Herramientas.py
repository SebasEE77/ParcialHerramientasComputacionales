print("BIENVENIDO A LA CAFETERIA DE LA UNIVERSIDAD PONTIFICIA JAVERIANA DE CALI")
print("Código producto Valor") 
print("0 Bandeja Paisa $ 20.000") 
print("1 Almuerzo Sencillo $ 12.000") 
print("2 Almuerzo Completo $ 15.000")
print("Usar el número -1 para terminar de ordenar")

def CafeteriaUniversidad():
    cedula = int(input("Ingrese su numero de cedula: "))
    rol = input("Ingrese el número segun su rol 1.estudiante 2.profesor: ")
    listaDeValor = [20000,12000,15000]
    listaProductos = ["Bandeja Paisa","Almuerzo sencillo","Almuerzo completo"]
    cantidad = []
    totalCompra = 0
    listaProductosFinales =[]
    listaValoresFinales =[]
    registro = {}
    codigo =int(input("Ingrese el código del producto que desea comprar: "))
    if codigo != len(listaProductos):
        while codigo != -1 :
            listaProductosFinales.append(listaProductos[codigo])
            listaValoresFinales.append(listaDeValor[codigo])
            registro[codigo]= listaProductos[codigo]
            codigo =int(input("Ingrese el codigo del producto que desea comprar:"))
        for valor in listaValoresFinales:
                    totalCompra += valor
        cantidad.append(len(listaProductosFinales))
        if rol == "1":
            becado = input("¿Haces parte de un programa de becas? ")
            if becado == "si" or becado == "Si":
                totalCompra= int(50*totalCompra/100)
                print("El Estudiante con cedula", cedula ,"debe pagar", totalCompra ,"por los productos", registro)
            else:
                totalCompra= int(totalCompra-30*totalCompra/100)
                print("El Estudiante con cedula", cedula ,"debe pagar", totalCompra ,"por los productos", registro)
        if rol == "2":
            totalCompra= int(totalCompra-20*totalCompra/100)
            print("El Profesor con cedula", cedula ,"debe pagar", totalCompra ,"por los productos", registro)
    else:
        print("Código no encontrado",codigo)


CafeteriaUniversidad()
        
    
    
