# Función que pide casillas al jugador (columna, renglón) @VALE π
def escoger_cartas(matrix):
    cartas = [] #Lista que guarda las cartas escogidas

    # Función que verifica que existan, no estén mostradas y no se repitan (regresa True/False)
    def exists():
        real = False
        if (row >= 0 and row < 6) and (column >= 0 and column < 6): #Primero checa si existe
            if not matrix[row][column][1]: #Luego si está mostrada
                if (len(cartas) != 0) and (cartas[0][0] == column) and (cartas[0][1] == row): #Finalmente, si se repite
                    print("Ya escogiste esa casilla, intenta de nuevo")
                else: #No se repite o es la primer carta
                    real = True
            else:
                print("Ya está mostrada esa casilla, intenta de nuevo")
        else:
            print("No existe esa casilla, intenta de nuevo")
        return real

    for i in range (1,3):
        while True: #do while pero pero adaptado a Python, pide carta hasta que sea una válida
            column = int(input("Ingresa la columna de la carta " + str(i) + ": ")) -1
            row = int(input("Ingresa el renglón de la carta " + str(i) + ": ")) -1
            valid = exists()
            if valid:
                break
        cartas.append([row, column])
    return cartas

    # print(matrix[cartas[0][0]][cartas[0][1]][0])   imprime la primera carta elegida
    # print(matrix[cartas[1][0]][cartas[1][1]][0])   imprime la segunda carta elegida

    #Pregunta al usuario si desea seguir jugando, (sí) se cambia de jugador @Lía

def continuar_juego ():
    global games
    if games==0:
        games+=1
        continuar= input("¿Deseas empezar a jugar? (Y/N)")
    else:
        continuar= input("¿Deseas seguir jugando? (Y/N)")
    if continuar.lower()=="y":
      return True #Lía, mejor haz que te regrese un boolean
    else:
      return False

# Mantener registro de las anotaciones de cada quién, ganador o empate @Lía
def aumentar_register (registro, jugador):
  #Le aumenta un punto a cada jugador
  registro[jugador-1]+= 1

#Función que muestra/imprime el tablero del memorama @MARTHA

def mostrar_tab (matrix):
  print("    [1] [2] [3] [4] [5] [6]")
  for x in range (0, 6): #Definen el largo y ancho del tablero
    print("[" + str(x+1) + "]  ", end='')
    for y in range (0, 6):
      if matrix[x][y][1] == False: #El número no es correcto, no se muestra
        print("–", end="   ")
      else: #El número es correcto, se muestra
        print(matrix[x][y][0], end="  ")
    print()

#Función que mantiene los valores visibles de ser iguales

def mostrar_iguales(matrix, cartas, registro, jugador):
  c1 = matrix[cartas[0][0]][cartas[0][1]][0]
  c2 = matrix[cartas[1][0]][cartas[1][1]][0]
  matrix[cartas[0][0]][cartas[0][1]][1] = True
  matrix[cartas[1][0]][cartas[1][1]][1] = True
  mostrar_tab(matrix)
  if c1 == c2:
    aumentar_register(registro,jugador)
  else: 
    matrix[cartas[0][0]][cartas[0][1]][1] = False
    matrix[cartas[1][0]][cartas[1][1]][1] = False
    print("Vuélvelo a intentar.")

#Función que define la posición de los números @JORGE
import random

def definir_numero():
    num=random.randrange(0,len(record))
    return record.pop(num)
    
record = [" 1"," 1"," 2"," 2"," 3"," 3"," 4"," 4"," 5"," 5"," 6"," 6"," 7"," 7"," 8"," 8"," 9"," 9","10","10","11","11","12","12","13","13","14","14","15","15","16","16","17","17","18","18"] #Estos son los datos que irán dentro del memorama

def determinar_posiciones(matrix):
  random.shuffle(record) #Revuelve el memorama
  random.shuffle(record)
  for x in range (0, 6):
      a=[] #Crea matriz de 6 números (tablero de 6x6)
      for y in range (0, 6):
          b = [definir_numero(),False] #Tiene un número y este se muestra solo si no es FALSE
          a.append(b) #b entra en a
      matrix.append(a)  #b está en toda la matriz

#Función que cierra el programa si ya no quedan más tarjetas por descubrir @JORGE

#Te regresa un boolean dependiendo de la operación.
def contar_vacios (matrix):
  suma=0
  for z in range(0,len(matrix)):
    for x in range (0,len(matrix[z])):
      if(matrix[z][x][1]== True):
        suma+=1
  if(suma==18*2): #Porque hay dos casillas de cada número
    return False
  else:
    return True

def determinar_ganador (registro):
  p1 = registro[0]
  p2 = registro[1]
  if p1==p2:
    return "¡Empatados a " + str(p1) + "!"
  elif p1>p2:
    return "Jugador 1: " + str(p1) + " pares encontrados, ¡Felicidades!\nJugador 2: " + str(p2) + " pares encontrados, por lo menos intentaste"
  else:
    return "Jugador 2: " + str(p2) + " pares encontrados, ¡Felicidades!\nJugador 1: " + str(p1) + " pares encontrados, por lo menos intentaste"

#Hola, aquí vamos a hacer el código del reto, ¿les parece si nos dividmos las funciones?
  # Necesistamos hacer un memorama con números del 1-18. 
  # Los valores deben aparecer dos veces
  
  #Funciones Vale π: ---------------------------------------------------------------------------------------------------------
    # Pedir casillas al jugador (linea, columna)                                                  ✔✔✔ - Verificado
    # Verificar que existan, no estén mostradas y no se repita                                    ✔✔✔ - Verificado
  #Funciones Martha: ---------------------------------------------------------------------------------------------------------
    # Mostrar el tablero                                                                          ✔✔✔ - Verificado
    # En caso de que las "cartas" sean iguales, va a mostrar (y mantener) los valores de la carta ✔✔✔ - Verificado
  #Funciones Lía: ------------------------------------------------------------------------------------------------------------
    # Pregunta al usuario si desea seguir jugando, (si) se cambia de jugador                      ✔✔✔ - Verificado
    # Mantener registro de las anotaciones de cada quién, ganador o empate                        ✔✔✔ - Verificado
  #Funciones Su servilleta: --------------------------------------------------------------------------------------------------
    # Determinar las posiciones de los números                                                    ✔✔✔ - Verificado
    # Cerrar el programa si ya no quedan tarjetas                                                 ✔✔✔ - Verificado
    # Mostrar el resultado del juego.                                                             ✔✔✔ - Verificado

games=0
def main ():
   global games
   registro=[0,0]
   jugador=1
   matrix= []
   determinar_posiciones(matrix)
   mostrar_tab(matrix)

   while (contar_vacios(matrix) and continuar_juego()):
     print("Turno del jugador " + str(jugador))
     cartas = escoger_cartas(matrix) #las cartas escogidas se guardan en la lista cartas
     mostrar_iguales(matrix, cartas, registro, jugador)
     if jugador ==2:
        jugador= jugador -1
     else:
        jugador = jugador +1
   print("El juego se acabó, <(╯︿╰)>")
   print(determinar_ganador(registro))



main() #CORRE EL MAIN DEL PROGRAMA!!!!!