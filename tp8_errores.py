####--------------------------------------------------------FUNCIONES------------------------------------------------------------####

###Recomiendo ver el programa e ir viendo dónde se utiliza cada una


def ffecha(fecha): #A esta función la cree para obtener la fecha en forma DD/MM/AAAA
    try:            
        dia = int(fecha[:2]) #PARA LOS PRIMEROS DOS ELEMENTOS, Y ASÍ HASTA EL ÚLTIMO.
        mes = int(fecha[2:4])
        año = int(fecha[4:])
        if dia <= 0 or dia > 31 or mes < 1 or mes > 12 or año > 2024 or año < 1900 or dia == '' or mes == '' or año == '': #Para salvarme de errores
            raise ValueError("Fecha no válida.")
        else: 
            fechaddmmaa = fecha[:2] + '/' + fecha[2:4] + '/' + fecha[4:] #Aquí pongo la fecha en el formato que quería     
    except ValueError as e:
        print(e)
        return False #Si me da un error, que me retorne un boleano cosa de poder usarlo cuando invoque la función en la función "crear_nuevo", donde creo un nuevo diccionario
    return fechaddmmaa


def notas(a, b, c):  #Esto también para darle un formato a las notas, ya que me gusta que diga que notas tiene en cada materia
    try:
        a= float(a) #pongo la opción de flotante porque puede tener un 1.5 por ejm
        b= float(b)
        c= float(c)
        return f"Matemáticas: {a}, Lengua: {b}, Física: {c}" #este es el formato que deseaba
        
    except ValueError as e:
        return "Las notas deben ser números", e #nada, solo tirar un mensaje, pero está para generalizar más, al invocar la función no se tanto
    except SyntaxError as e:
        return "Error de sintaxis", e


def crear_alumno(): #LA FUNCIÓN QUE ME CREA UN DICCIONARIO CON LA INFORMACIÓN DEl ALUMNO
    nombre= input("Ingrese el nombre del nuevo alumno: ") #Ingresar el  nombre, dejé pasar el error del caracter vacío, aunque no sé si no toma como error, idem abajo
    nombre= nombre.capitalize()#capitalizo para que una vez agregado, lo pueda buscar según la estructura del programa
    apellido= input("Ingrese el apellido del nuevo alumno: ")
    apellido= apellido.capitalize()
    while True:
        try:            
            dni= int(input("Ingrese el DNI del nuevo alumno: "))
            if dni < 0: 
                raise ValueError("DNI no válido.")
            break
        except ValueError as e:
            print(e)
    fecha_v= False #creo la variable con valor booleano False para poder usarla sin tantos "errores" cometidos por el usuario
    while not fecha_v: #Esto es una contrarecíproca, mientras la fecha en la variable fecha sea errónea, seguirá andando el ciclo hasta que sea correcta según la estructura de la función ffecha
        fe= input("Ingrese fecha ddmmaaaa: ")
        fecha= ffecha(fe) #esta es la variable fecha, donde uso la función que definí arriba
        if fecha: #si se cumple las condiciones dadas por la función (if dia <= 0 or dia > 31 or mes < 1 or mes > 12 or año > 2024 or año < 1900)
                  #entonces recién la variable fecha_v  toma el valor True y el ciclo deja de andar, por el cumplimiento de la contrarecíproca 
            fecha_v= True
    
    tutor= input("Ingrese el tutor del nuevo alumno: ")
    while True: #un ciclo para evitar errores, nada más, podrá observarse en el try y en el if
        try:            
            notas1= float(input("Ingrese la nota de matemáticas: "))
            notas2= float(input("Ingrese la nota de lengua: "))
            notas3= float(input("Ingrese la nota de física: "))
            #En la función que definí como notas(a,b,c) ya contemplo algunos errores, pero aquí con el ciclo while True 
            #hago posible que siga andando hasta tener un valor correcto
            if notas1 < 0 or notas2 < 0 or notas3 < 0  or notas1 == '' or notas2 == '' or notas3 == '' or notas1 > 10 or notas2 > 10 or notas3 > 10: #aquí lo contemplo de nuevo
                print("Notas no válidas.")
                continue #con el continue logro que me siga pidiendo ingresar si las notas no son válidas.
            
            break #al ser válidas según la función que definí, me cierra el ciclo
        except ValueError as e: 
            print(e)
    nota= notas(notas1, notas2,notas3)
    while True: #lo mismo practicamente que lo anterior
        try:            
            falta= float(input("Ingrese la cantidad de faltas del alumno: ")) #cuento la llegada tarde jaja
            if falta < 0 or falta == '':
                raise ValueError("No válida.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:            
            amo= int(input("Ingrese la cantidad de amonestaciones del nuevo alumno: ")) 
            if amo < 0 or amo == '': 
                raise ValueError("No válido.")
            break
        except ValueError as e:
            print(e)
    
    nuevo_alumno = {
        "Nombre": nombre ,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha,
        "Tutor": tutor,
        "Notas": nota,
        "Faltas": falta,
        "Amonestaciones": amo
    }
    return nuevo_alumno

def modificardiccionario(diccionario, primerdatoubica, segundatoubi, dato_cambiar, nuevovalor): 
    #la idea de formular la función así es por la estructura del diccionario, 
    #ya que es un diccionario de la forma dic= {"Alumnos" , [ {...} , {...} ] }, donde la variable -primerdatoubi- es "Alumnos"
    #la variable -segundatoubi- son los keys que están dentro de la los diccionarios dentro de la lista (Nombre, DNI, etc)
    #la variable -nuevovalor- es el valor que voy a cambiar
    #necesito que me cambie el valor dato_cambiar
    for alumno in diccionario[primerdatoubica]: #recorroy busco en este caso en datos["Alumnos"]
        if segundatoubi in alumno and alumno[segundatoubi] == dato_cambiar: #siguiendo la estructura del  diccionario, segundatoubi = Nombre, dni, etc
                        #si un dato está dentro de los keys de los diccionarios anidados y además a ese key le corresponde el dato a cambiar
            alumno[segundatoubi] = nuevovalor #lo actualizo
            return True #retorno un true si pasa eso, porque solo necesit actualizar
    return False #si no pasa nada de eso, retorno un false
    
def eliminardicc(diccionario, primeroubi, opcion, variable):#defino esta función con el fin de eliminar el diccionario anidado correspondiente a un alumno
    #la función solicita el diccionario. El valor -prieroubi- está así por cómo está definido el diccionario, en este caso sería "Alumnos"
    #El valor -opcion- es la opción que le doy al usuario para acceder a los datos del alumno,  por nombre, DNI o apellido.
    #El valor -variable- el el dato de la opción elegida por el usuario. Por ejemplo, al elegir DNI como opción y al poner un DNI correcto, la función me eliminará el diccionario correspondiente a este DNI
    
    for alumno in diccionario[primeroubi]: #Recorro y me fijo, como en las funciones anteriores
        if alumno[opcion] == variable: #Acá me fijo si el valor alumno[opcion], que podría ser alumno[DNI], por ejm
            #De ser igual el dato del diccionario anidado y dentro de la lista al dato alumno[DNI].
            #Si variable= 123456 y alumno[DNI]= 123456, elimino ese diccionario y retorno un booleano para que sí se pueda modificar
            diccionario[primeroubi].remove(alumno)
            return True
        elif opcion == "DNI":
            try:
                if alumno[opcion] == int(variable):
                    diccionario[primeroubi].remove(alumno)
                return True
            except ValueError:
                return False
    return False            

####----------------------------------------------------HASTA AQUÍ FUNCIONES--------------------------------------------------------####


datos= {"Alumnos" : [ {
"Nombre": "Nicolas",
"Apellido" : "Faur",
"DNI" : 39364617,
"Fecha de nacimiento": "12/10/1995",
"Tutor" : "Padre de Nico",
"Notas" : "Matemáticas: 10, Lengua: 7, Física: 10",
"Faltas" : 19,
"Amonestaciones" : 15
}, 
{"Nombre": "Maria",
"Apellido" : "Moco",
"DNI" : 123456,
"Fecha de nacimiento": "11/11/1999",
"Tutor" : "Madre de María",
"Notas" : "Matemáticas: 9, Lengua: 10, Física: 8",
"Faltas" : 2,
"Amonestaciones" : 0}
]
} 

while True:
    opcionA= input("Desea acceder a los datos por nombre, apellido, DNI o presione (*) para salir: ")
    if opcionA == "*":
        print("Decidió salir del programa")
        break
    opcion= opcionA.lower() #convierto todo a minúsculas para comparar mejor
    ## A LO LARGO DEL PROGRAMA HAGO ESTOS CAMBIOS PARA PODER COMPARAR.
    #Convierto todo a minúsculas, luego convierto la primera letra a mayúscula, excepto en el DNI donde convierto todo a mayúsculas
    #Al hacer eso, podré acceder a los datos proporcionados por el diccionario, ya que los strings deben ser iguales.

    if opcion == "dni": #como convertí lo ingresado a minúsculas, si la opción es dni, convierto todo a mayúsculas
          opcion = opcion.upper()        
    if opcion == "apellido" or  opcion == "nombre" or opcion == "DNI": #Aquí, cualquieras de estas opciones están contempladas con .lower() o .upper()
            variable= input(f"Ingrese el {opcion} que desea buscar: ") #Ingreso el nombre, dni o apellido del alumno para buscarlo
            encontrar= False #creo la variable encontrar para ver si encontró un dato con lo proporcionado en la variable -variable-
            if opcion != "DNI": #Si la opción no era DNI, entonces:
                variable = variable.capitalize() #convierto la primera letra en mayúscula, cosa de que si al ingresar -nicolas-, transforme a -Nicolas-                
            for alumno in datos["Alumnos"]: #recorro y busco, como en las funciones
                    #print(alumno)
                if opcion != "DNI": #Si la opción es nombre o apellido
                    if variable == alumno[opcion.capitalize()]: #Busco el nombre o apellido proporcionado en los diccionarios anidados que están dentro del diccionario de alumnos
                                                                #El .capitalize() es porque los datos están todos con la primera letra mayúscula
                        print(f"Datos correspondientes a {opcion} = {variable}: ") #nada más que mostrar
                        print()
                        print(alumno)
                        print("---------------------------------------------------------------------")
                        encontrar= True #si pasó esto, entonces quiere decir que sí encontre un dato, entonces le asigno un True a la variable encontrar     
                elif opcion == "DNI": 
                    if int(variable) == alumno["DNI"]: #Aquí me fijo si el DNI escrito en el input de variable, está en la parte del diccionario correspondiente a los DNI
                                                        #Está el int(variable) porque anteriormente la variable se convirtió a strings, por medio de los conversores de caracteres
                        print(f"Datos correspondientes a {opcion} = {variable}: ")
                        print()
                        print(alumno)
                        print("---------------------------------------------------------------------")
                        encontrar= True #Lo mismo que arriba
            if encontrar == True: #SI ENCONTRÉ UN DATO CON LO QUE ESCRIBÍ, ENTONCES OFREZCO MODIFICAR UN DATO O EXPULSAR AL ALUMNO
                si= input("Desea modificar algún dato del alumno?, precione S: ") #pregunta si desea modificar
                si=si.lower() #convierte a minúscula la elección, para poder acceder al siguiente if, más fácilmente
                if si == "s":
                    print()
                    cambiar= input("Ingrese lo que quieres cambiar (nombre, dni, notas, etc): ") #DOY LA POSIBILIDAD DE CAMBIAR CUALQUIER DATO DEL ALUMNO
                    print()
                    cambiar= cambiar.lower()
                    if cambiar != "dni": #Lo mismo que más arriba
                        cambiar = cambiar.capitalize()
                    else:
                        cambiar = cambiar.upper()
                    if cambiar == "Notas": #Si quiero cambiar las notas
                        while True: #para poder poner notas certeras nada más, nada de notas negativas o mayores a 10
                            try:            
                                notas1= float(input("Ingrese la nueva nota de matemáticas: "))
                                notas2= float(input("Ingrese la nueva nota de lengua: "))
                                notas3= float(input("Ingrese la nueva nota de física: "))
                                if notas1 < 0 or notas2 < 0 or notas3 < 0  or notas1 == '' or notas2 == '' or notas3 == '' or notas1 > 10 or notas2 > 10 or notas3 > 10: 
                                    print("Notas no válidas.")
                                    continue
                                break
                            except ValueError as e: #para ver el error (no sé si está bien)
                                print(e)
                        nuevovalor= notas(notas1, notas2, notas3) #INVOCO LA FUNCIÓN notas(a,b,c), definida antes
                    elif cambiar == "Fecha de nacimiento": #Esto es lo mismo que la función crear_alumno(), donde me voy por la contrarecíproca
                        fecha_v= False 
                        while not fecha_v: 
                            fe= input("Ingrese nueva fecha de nacimiento ddmmaaaa: ")
                            fecha= ffecha(fe) 
                            if fecha: 
                                fecha_v= True
                        nuevovalor= fecha
                    elif cambiar == "DNI": #Solo para cambiar DNI, lógica análoga a las anteriores
                        while True:
                            try:            
                                dni= int(input("Ingrese el DNI del nuevo alumno: "))
                                if dni < 0: 
                                    raise ValueError("DNI no válido.")
                                break
                            except ValueError as e:
                                print(e)
                        nuevovalor= dni    
                    elif cambiar == "Faltas":
                        while True: #lo mismo practicamente que lo anterior
                            try:            
                                falta= float(input("Ingrese la cantidad de faltas del alumno: ")) #cuento la llegada tarde jaja
                                if falta < 0 or falta == '':
                                    raise ValueError("No válida.")
                                break
                            except ValueError as e:
                                print(e)
                        nuevovalor= falta
                    elif cambiar == "Amonestaciones":
                        while True:
                            try:            
                                amo= int(input("Ingrese la cantidad de amonestaciones del alumno: ")) 
                                if amo < 0 or amo == '': 
                                    raise ValueError("No válido.")
                                break
                            except ValueError as e:
                                print(e)
                        nuevovalor= amo
                    else:
                        nuevovalor=  input(f"Ingrese el nuevo dato para {cambiar}: ").capitalize() #Esto para cambiar apellido, nombre o tutor
                    opcion= opcion.lower() #nuevamente hago el juego de la conversión de caracteres, para acceder a elementos en la iteración
                    if opcion != "dni":
                        opcion= opcion.capitalize() #hago que la opción ingresada antes sea la primer letra con mayúscula, por ejm Nombre
                    else: 
                        opcion= opcion.upper()
                    ##print(opcion, variable, cambiar, type(opcion), type(variable), type(cambiar))
                    for i in range(len(datos["Alumnos"])): #recorro y me fijo según la estructura del diccionario
                        ##print(variable, datos["Alumnos"][i][opcion])
                    #El tema aquí fue encontrar el dato del alumno, por ejm si el DNI era 39364617, necesitaba buscar ese 39364617, o Nicolas, o un apellido
                        if variable == datos["Alumnos"][i][opcion]: #la búsqueda es en la estructura, recurdar que variable era un string
                            ##print("----------",datos["Alumnos"][i][opcion])
                            a = i
                            dato_acambiar= datos["Alumnos"][i][cambiar] #AQUÍ ENCONTRÉ EL VALOR A CAMBIAR
                            ##print(dato_acambiar)
                        if opcion == "DNI" and int(variable) == datos["Alumnos"][i][opcion]: #Esto porque cuando ingreso DNI como opción, al ser strings lo convierto a entero y recién podré encontrarlo en el diccionario, ya que ahí está con type=int
                            ##print("----------",datos["Alumnos"][i][opcion])
                            a = i
                            dato_acambiar= datos["Alumnos"][i][cambiar] ##AQUÍ ENCONTRÉ EL VALOR A CAMBIAR
                            ##print(dato_acambiar)
                    
                    #FIJARSE QUE EN CADA IF ELIF hay una variable llamada -nuevovalor-, que es un input para que me ingrese el nuevo dato correspondiente a lo que eligió
                           
                    modificardiccionario(datos, "Alumnos", cambiar, dato_acambiar, nuevovalor)
                    print("------------------------------------------------------------------------------------------------------")
                    print(f"Alumno {opcion} = {variable}, cambiando dato de {cambiar} = {dato_acambiar} a {cambiar} = {nuevovalor} ")
                    print()
                    print(f"Nuevos datos del alumno {opcion} = {variable}: ")
                    print()
                    print(datos["Alumnos"][a]) 
                    print("------------------------------------------------------------------------------------------------------")

                opcion= opcion.lower()    
                if opcion != "dni":
                    opcion= opcion.capitalize() #hago que la opción ingresada antes sea la primer letra con mayúscula, por ejm Nombre
                else: 
                    opcion= opcion.upper()
                nose= input("Desea expulsar al alumno (borrar sus datos)?, precione S: ")
                print()
                nose=nose.lower()
                ##print(opcion, variable, type(opcion), type(variable))
                
                if nose == "s":    
                    eliminardicc(datos, "Alumnos", opcion, variable)
                    print(f"Alumno con {opcion} = {variable} eliminado.")
                    print()    
                    print("Nuevos datos actualizados: ")
                    print()
                    print(datos)
                    print("-----------------------------------------------------------------------")
                    
            if not encontrar: #Si no encontró el dato proporcionado como variable, entonces me da la opción de agregar dicho alumno
                 agregar= input(f"Alumno  {variable} no encontrado, desea agregarlo?, ingrese S: ")
                 
                 if agregar.lower() == "s":
                    nuevo= crear_alumno() #USO LA FUNCIÓN CREAR_ALUMNO, QUE ME CREA UN DICCIONARIO CON LOS DATOS DEL NUEVO ALUMNO
                    print("-----------------------------------------------------------------------")
                    print("Los datos del nuevo alumno son: ")
                    print()
                    print(nuevo)
                    print("-----------------------------------------------------------------------")
                    datos["Alumnos"].append(nuevo) #Añado el alumno al diccionario.        
    else: 
        print("Debe ingresar una opción válida.")
    


