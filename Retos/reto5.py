######################## Reto empresa ticknet.corp ###############################
# Autor: German Homero Moran Figueroa
# Grupo de programacion 51654 

# Librerias Usadas
import os
import numpy as np
import math
from io import open

# Funcion Menu
def menu(listamenu):
    os.system('cls')
    print("")
    print("",str("1."),listamenu[0],"\n", 
    str("2."),listamenu[1],"\n",
    str("3."),listamenu[2],"\n",
    str("4."),listamenu[3],"\n",
    str("5."),listamenu[4],"\n",
    str("6."),listamenu[5],"\n",
    str("7."),listamenu[6],"\n")
    opmenu = int(input("Elija una opción: "))
    return opmenu

# Funcion para hacer el intercambio de las opciones del menu
def menuop6(listamenu):                           
    opfavorita = int(input("Seleccione opción favorita: "))
    if (opfavorita >= 1 and opfavorita <=5):
        #os.system('cls')
        print("Confirmacion de Usuario, responda las preguntas de control: \n")
        ad1 = int(input("Si me giras pierdo tres unidades por eso debes colocarme siempre de pie: "));
        if ad1 ==5:
            ad2 = int(input("Me separaron de mi hermano siamés, antes era un ocho y ahora soy un: "));
            if ad2 != 4:
                print("Error")
                
            else:
                aux = listamenu[0]
                listamenu[0] = listamenu[(opfavorita-1)]
                listamenu[(opfavorita-1)] = aux
                 
        else:
            print("Error")
               
    else:
        print("Error")
        exit()

# Funcion para realizar el cambio de la contraseña
def CambioContrasena(contrasena):
    print("")
    val_contrasena = int(input("Diguite la contraseña actual: "))
    if contrasena == val_contrasena:
        nueva_contra = int(input("Ingrese la nueva contraseña: "))
        # Despues de introudcir la nueva contraseña , se debe validar que sea diferente a la actual
        while nueva_contra == contrasena:
            nueva_contra = int(input("La contraseña debe ser diferente, ingrese la nueva contraseña: "))
            if nueva_contra != contrasena:
                break
        
    else:
        # La contraseña ingresada no coincide con la actual
        print("Error")
        exit()
    
    return nueva_contra

# Funcion para el ingreso de coordenadas
def ingresar_cordenadas():
    # Se crea la matriz donde se almacenaran las coordenadas
    m_cordenadas = np.zeros((3, 2))
    # Dimensiones de la matriz
    dime = m_cordenadas.shape
    
    #Se establecen los rangos deacuerdo al penultimo digito del grupo FP: 51654
    # Latitud rango: Superior - Inferior  , 6.580
    rest_lat = [10.462, 9.757]

    #Longitud rango: Occidente- Oriente  , -72.970
    rest_lng = [-72.987, -73.623] 

    for i in range(dime[0]): 
        for j in range(dime[1]):
            if j == 0:
                lat = round(float(input("Ingrese la latitud: ")),3)
                if lat > rest_lat[0] or lat < rest_lat[1]:
                    print("Error coordenada")
                    exit()
                else:
                    m_cordenadas[i][j] = lat
            
            elif j==1:
                lng = round(float(input("Ingrese la longitud: ")),3)
                if lng > rest_lng[0] or lng < rest_lng[1]:
                    print("Error coordenada")
                    exit()
                else:
                    m_cordenadas[i][j] = lng


    return m_cordenadas

# Funcion para localizar las Zonas Wi-Fi mas cercanas decuerdo a la distancia y al numero de usuarios conectados
def zonas_wifi_cercanas(cord_lat, cord_lng, paz):
    
    # Se define la matriz donde se almacenan las ubicaciones de la zona WI-FI con la respectiva carga de usuarios
    #paz = np.array([[10.348, -73.051, 0],[10.171, -73.136, 0],[10.259, -73.069, 67],[10.350, -73.043, 45]])
    #print(paz)
    #print(len(paz))

    # Cordenadas base  registradas por el usuario (Lat1 - Lng 1)
    lat = cord_lat
    lng = cord_lng
    distancias = []                                 # Lista para almacenar las distancias a las zonas Wi-Fi
    users = []                                      # Lista para almacenar los respectivos Usuarios
    idx = []
    r=6371                                          # Radio de la tierra en KM
    #print(r)
    for x in range(len(paz)):
        # Calculo los respectivos deltas
        dlat = math.radians((paz[x][0] - lat))       #Lat2- Lat1
        dlon = math.radians((paz[x][1] - lng))       #Lng2 - Lng1
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) * math.cos(math.radians(paz[x][0])) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        # calculo la distancia
        d = r * c
        #print("La distancia en kilometros es: ", round(d,3))
        idx.append(x)
        users.append(paz[x][2])
        distancias.append(round(d,3))
    

    # Creamos el diccionario con distancias y usuarios
    dictionary = dict(zip( distancias, users))
    #print(dictionary)

    # Ordeno el diccionario deacuerdo a las distancias de menor - mayor
    ord_dis = (sorted(dictionary.items()))

    # Selecciono las 2 distancias mas cercanas
    ord_num_users = ord_dis[0:2]
    
    # Ordeno las 2  distancias deacuerdo al numero de usuarios
    ord_num_users.sort(key = lambda x: x[1])


    #print(ord_num_users)

    return ord_num_users, distancias


# Munu Principal -  Lista
listamenu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar Zona Wifi mas cercana",
"Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo",
"Elegir opción de menú favorita","Cerrar sesión"]


#################################### RETO 1 #####################################################
# Variables Globales
usuario = 51654
clave = 45615
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
new_user = int(input("Ingrese el usuario: "))


# Validamos el usuario ingresado
if(new_user != usuario):
    print("Error")
    exit()

# Validamos la contraseña ingresada
new_pass = int(input("Ingrese la contraseña: "))
if (new_pass != clave):
    print("Error")
    exit()

# Obtenemos el captcha a travez de operaciones aritmeticas  FP: 51654
captcha_1 = 654;  
captcha_2 = (6*5)+((-4*6)/4)+1+(-5*4);                # 5
captcha_3 = captcha_1 + captcha_2;                    #654+5 =659

# Solicitamos el ingreso del Captcha por parte del usuario
captcha_user = int(input("Ingrese el captcha: "))


# Validamos el captcha ingresado por el usuario
if(captcha_user == captcha_3):
    print("Sesión iniciada")
    contint = 0                     #cuenta el numero de intens fallido y se sale del menu al ser igual a 3
    opmenu = 1                      #se inicializa en 1 para que entre por primera vez al while 
    bandera = False                 #Bandera para controlar que  se halla llenado las cordenadas inicialmente
    bandera2= False                 #Bandera para controlar que ya se localizó una zona Wi-Fi Cercana
    bandera3= False                 #Bandera para controlar y leer un archivo externo
    rest_lat = [10.462, 9.757]      # Latitud rango: Superior - Inferior
    rest_lng = [-72.987, -73.623]   #Longitud rango: Oriente : Occicente

    # Se define la matriz donde se almacenan las ubicaciones de la zona WI-FI con la respectiva carga de usuarios
    if bandera3 == False:
        paz = np.array([[10.348, -73.051, 0],[10.171, -73.136, 0],[10.259, -73.069, 67],[10.350, -73.043, 45]])
    else:
        paz = np.loadtxt('matriz.txt', delimiter=',')

    # Calculo de la Velocidad promedio
    v_moto = 14.44                  #m/s
    v_bici = 3.33                   #m/s

    zw1 = []                        # Lista que gurdara informacion de la Zona Wi-Fi  1
    dis = []                        # Lista que gurada informacion de la distancia y recorrido a la Zona Wi-Fi 1
    while (opmenu != 7 and contint !=3): 
        opmenu = menu(listamenu)
        # controlo que las opciones del menu esten entre 1 y 7
        if (opmenu > 7) or (opmenu <= 0): 
            contint +=1
            print("Error")
        
        if opmenu == 1:
            print(f"Usted ha elegido la opción {opmenu}") 
            clave = CambioContrasena(clave)

        if opmenu == 2:
            print(f"Usted ha elegido la opción {opmenu}") 
            if bandera == False:
               # Aqui retorno la matriz con las coordenadas 
               a=ingresar_cordenadas()
               bandera = True

            else:
                print("Estas son las cordenadas actualmente almacenadas en el sistema")
                print("coordenada [latitud, longitud] 1 : ", a[0])
                print("coordenada [latitud, longitud] 2 : ", a[1])
                print("coordenada [latitud, longitud] 3 : ", a[2])
                print("la coordenada 2 es la que esta mas al sur")
                print("coordenada 1 es el promedio de todos los puntos")
                cor_modif = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))
                if cor_modif == 0:
                    print("")

                #Cambio de la primera cordenada
                elif cor_modif==1:
                    print("")
                    lat = round(float(input("Ingrese la latitud: ")),3)
                    if (lat > rest_lat[0] or lat < rest_lat[1]):
                        print("Error coordenada")
                        exit()
                    else:
                        a[0][0]=lat
                
                    lng = round(float(input("Ingrese la longitud:")),3)
                    if lng > rest_lng[0] or lng < rest_lng[1]:
                        print("Error coordenada")
                        exit()
                    else:
                        a[0][1] = lng

                # Cambio de la segunda cordenada
                elif cor_modif ==2:
                    print("")
                    lat = round(float(input("Ingrese la latitud: ")),3)
                    if (lat > rest_lat[0] or lat < rest_lat[1]):
                        print("Error coordenada")
                        exit()
                    else:
                        a[1][0]=lat
                
                    lng = round(float(input("Ingrese la longitud:")),3)
                    if lng > rest_lng[0] or lng < rest_lng[1]:
                        print("Error coordenada")
                        exit()
                    else:
                        a[1][1] = lng
        
           # Cambio de la tercera cordenada
                elif cor_modif == 3:
                        print("")
                        lat = round(float(input("Ingrese la latitud: ")),3)
                        if (lat > rest_lat[0] or lat < rest_lat[1]):
                            print("Error coordenada")
                            exit()
                        else:
                            a[2][0]=lat
                        
                        lng = round(float(input("Ingrese la longitud:")),3)
                        if lng > rest_lng[0] or lng < rest_lng[1]:
                            print("Error coordenada")
                            exit()
                        else:
                            a[2][1] = lng
                            
                # Si el usuario digita una opcion diferente
                else:
                    print("Error actualización")
                    exit()

        if opmenu == 3:
            #print(f"Usted ha elegido la opción {opmenu}")

            # Verficamos que el usuario haya ingresado anteriormente las coordenadas de las ubicaciones
            if bandera == False:
                print("Error sin registro de coordenadas")
                exit()
            
            else:
                print("coordenada [latitud, longitud] 1 : ", a[0])
                print("coordenada [latitud, longitud] 2 : ", a[1])
                print("coordenada [latitud, longitud] 3 : ", a[2])
                opc_dit = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión"))
                # Verficamos que las entradas sean las correctas

                # Si el User eleje la opcion 1
                if opc_dit == 1:
                    cord_lat = a[0][0]
                    cord_lng = a[0][1]
                    
                    #print(paz)
                    # Llamamos a la funcion para localizar las zonas wifi cercanas
                    zw_near, distancias= zonas_wifi_cercanas(cord_lat,cord_lng,paz)
                    
                    # Cambia el estado de la bandera cuando ya se calculo la distancia
                    bandera2 = True

                    b = distancias.index(zw_near[0][0])
                    c = distancias.index(zw_near[1][0])

                    # Agregamos informacion de la zona Wi-Fi 1  a la lista zw1
                    zw1.append(paz[b][0])
                    zw1.append(paz[b][1])
                    zw1.append(zw_near[0][1])

                    # Agregamos infromaicon de la distancia y recorrido a la lista dis
                    dis.append(zw_near[0][0])
                    print("zonas wifi cercanas con menos usuarios")
                    print(f"La zona wifi 1: ubicada en [{paz[b][0]},{paz[b][1]}] a {zw_near[0][0]} m, tiene e promedio {zw_near[0][1]} usuarios")
                    print(f"La zona wifi 2: ubicada en [{paz[c][0]},{paz[c][1]}] a {zw_near[1][0]} m, tiene e promedio {zw_near[1][1]} usuarios")
                    op_ind = int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                    if op_ind == 1:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[0][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[0][0]/v_bici

                        # Correguir esta parte
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {round(t_moto,3)} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")

                        # Agregamos informacion de un medio de trasporte y el tiempo promedio
                        dis.append('moto')
                        dis.append(round(t_moto,3))

                        s = int(input("Presione 0 para salir"))
                    elif op_ind ==2:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[1][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[1][0]/v_bici
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {round(t_moto,3)} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")
                        s = int(input("Presione 0 para salir"))
                    else:
                        print("Error zona wifi")
                        exit()
                
                elif opc_dit == 2:
                    cord_lat = a[1][0]
                    cord_lng = a[1][1]
                    
                    # Llamamos a la funcion para localizar las zonas wifi cercanas
                    zw_near, distancias= zonas_wifi_cercanas(cord_lat,cord_lng,paz)

                    # Cambia el estado de la bandera cuando ya se calculo la distancia
                    bandera2 = True

                    b = distancias.index(zw_near[0][0])
                    c = distancias.index(zw_near[1][0])

                    # Agregamos informacion de la zona Wi-Fi 1  a la lista 
                    zw1.append(paz[b][0])
                    zw1.append(paz[b][1])
                    zw1.append(zw_near[0][1])

                    # Agregamos infromaicon de la distancia y recorrido
                    dis.append(zw_near[0][0])

                    print("zonas wifi cercanas con menos usuarios")
                    print(f"La zona wifi 1: ubicada en [{paz[b][0]},{paz[b][1]}] a {zw_near[0][0]} m, tiene e promedio {zw_near[0][1]} usuarios")
                    print(f"La zona wifi 2: ubicada en [{paz[c][0]},{paz[c][1]}] a {zw_near[1][0]} m, tiene e promedio {zw_near[1][1]} usuarios")
                    op_ind = int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                    if op_ind == 1:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[0][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[0][0]/v_bici

                        # Correguir esta parte
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {round(t_moto,3)} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")

                        # Agregamos informacion de un medio de trasporte y el tiempo promedio
                        dis.append('moto')
                        dis.append(round(t_moto,3))

                        s = int(input("Presione 0 para salir"))
                    elif op_ind ==2:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[1][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[1][0]/v_bici
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {round(t_moto,3)} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")
                        s = int(input("Presione 0 para salir"))
                    else:
                        print("Error zona wifi")
                        exit()
                    

                elif opc_dit == 3:
                    cord_lat = a[2][0]
                    cord_lng = a[2][1]
                    
                    # Llamamos a la funcion para localizar las zonas wifi cercanas
                    zw_near, distancias= zonas_wifi_cercanas(cord_lat,cord_lng,paz)
                    b = distancias.index(zw_near[0][0])
                    c = distancias.index(zw_near[1][0])

                    # Cambia el estado de la bandera cuando ya se calculo la distancia
                    bandera2 = True

                    # Agregamos informacion de la zona Wi-Fi 1  a la lista 
                    zw1.append(paz[b][0])
                    zw1.append(paz[b][1])
                    zw1.append(zw_near[0][1])

                    # Agregamos infromaicon de la distancia y recorrido
                    dis.append(zw_near[0][0])
                    print("zonas wifi cercanas con menos usuarios")
                    print(f"La zona wifi 1: ubicada en [{paz[b][0]},{paz[b][1]}] a {zw_near[0][0]} m, tiene e promedio {zw_near[0][1]} usuarios")
                    print(f"La zona wifi 2: ubicada en [{paz[c][0]},{paz[c][1]}] a {zw_near[1][0]} m, tiene e promedio {zw_near[1][1]} usuarios")
                    op_ind = int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                    if op_ind == 1:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[0][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[0][0]/v_bici

                        # Correguir esta parte
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {c} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")

                        # Agregamos informacion de un medio de trasporte y el tiempo promedio
                        dis.append('moto')
                        dis.append(round(t_moto,3))

                        s = int(input("Presione 0 para salir"))
                    elif op_ind ==2:
                        # Calculo del tiempo medio - utilizando moto
                        t_moto = zw_near[1][0]/v_moto
                        # Calculo del tiempo medio utilizando bicicleta
                        t_bici = zw_near[1][0]/v_bici
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        # Tiempos medios
                        print(f"Tiempo promedio en moto: {round(t_moto,3)} seg")
                        print(f"Tiempo promedio en bicicleta: {round(t_bici,3)} seg")
                        s = int(input("Presione 0 para salir"))
                    else:
                        print("Error zona wifi")
                        exit()
 
                else:
                    print("Error ubicación")
                    exit()
            


        if opmenu == 4:
            #print(f"Usted ha elegido la opción {opmenu}") 
            if bandera == False and bandera2 == False:
                print("Error de alistamiento")
                exit()
            else:
                informacion = {'actual': [cord_lat, cord_lng],
                'zonawifi1': zw1,
                'recorrido': dis}
                print(informacion)
                
                i = int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))
                if i == 1:
                    print("Exportando archivo")
                    # Exportamos el archivo  con la infromacion a un Formato de texto plano.
                    archivo_exportar = open("informacion.txt","w")
                    archivo_exportar.write(str(informacion))
                    archivo_exportar.close()
                    exit()
                else:
                    print("")



        if opmenu == 5:
            #print(f"Usted ha elegido la opción {opmenu}")
            bandera3 = True
            op5= int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")) 
            

        if opmenu == 6: # en esta opcion se puede hacer una funcion (opmenu6(listamenu)) para que se haga el intercambio de la opcion 1 con la opcion de favorito que seleccione la persona variable temporal "aux".
            menuop6(listamenu) 
            os.system('cls')
   
        if (opmenu == 7):
            print("Hasta pronto")
            exit()
    
    # funciona cuando el usuario por primera vez digita la opcion salir
    if (opmenu == 7):
        print("Hasta pronto") 
        exit()                
    
    
else:
    print("Error")
    exit()



    