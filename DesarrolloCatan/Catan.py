from Cartas.CartasCatan import *
from random import *

#secuencia para recorrer todas las casillas del tablero en un orden determinado
secComandos = [0,2,3,4,5,0,0,1,2,2,3,3,4,4,5,5,0,0]
secA2 = [4,4,3,3,2,2,1,1,0,0,5,4,4,3,2,1,0,4]
secK2 = [3,3,2,2,1,1,0,0,5,5,4,3,3,2,1,0,5,3]
secI2 = [2,2,1,1,0,0,5,5,4,4,3,2,2,1,0,5,4,2]
secG2 = [1,1,0,0,5,5,4,4,3,3,2,1,1,0,5,4,3,1]
secE2 = [0,0,5,5,4,4,3,3,2,2,1,0,0,5,4,3,2,0]
secC2 = [5,5,4,4,3,3,2,2,1,1,0,5,5,4,3,2,1,5]
secDados = [5,2,6,3,8,10,9,12,11,4,8,10,9,4,5,6,3,11]
contador = 0
inicioCP = [0,0,0,0]

#variables de generar MineralRandom
contM = 4
contO = 4
contT = 4
contL = 3
contR = 3
contD = 1

#variables de los jugadores

#variables bucles del programa
okWhileMapa = False

#----------------CREACION DE LA CLASE TABLERO-----------------------------

class Tablero():

#----------------INSERCION VARIABLES-----------------------------------
    def __init__(self,raiz):

        self.Sup = None
        self.SupDer = None
        self.InfDer = None
        self.Inf = None
        self.InfIzq = None
        self.SupIzq = None
        self.clave = raiz

#----------------METODOS INSERCCION-----------------------------------
    #inserta la union entre un nodo y el nodo superior y viceversa
    def insSup(self,newNodo):
        if self.Sup == None:
            self.Sup = newNodo
            newNodo.insInf(self)
            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta la union entre un nodo y el nodo superior derecho y viceversa
    def insSupDer(self,newNodo):
        if self.SupDer == None:
            self.SupDer = newNodo
            newNodo.insInfIzq(self)

            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta la union entre un nodo y el nodo inferior derecho y viceversa
    def insInfDer(self,newNodo):
        if self.InfDer == None:
            self.InfDer = newNodo
            newNodo.insSupIzq(self)
            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta la union entre un nodo y el nodo inferior y viceversa
    def insInf(self,newNodo):
        if self.Inf == None:
            self.Inf = newNodo
            newNodo.insSup(self)
            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta la union entre un nodo y el nodo inferior izquierdo y viceversa
    def insInfIzq(self,newNodo):
        if self.InfIzq == None:
            self.InfIzq = newNodo
            newNodo.insSupDer(self)
            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta la union entre un nodo y el nodo superior izquierdo y viceversa
    def insSupIzq(self,newNodo):
        if self.SupIzq == None:
            self.SupIzq = newNodo
            newNodo.insInfDer(self)
            #print(self.clave,"<--->",newNodo.clave, end=" ")
        else:
            pass
    #inserta una lista con los datos iniciales de casilla en un nodo
    def InsLista(self):
        global jugActivo
        caminos = [0,0,0,0,0,0]
        ciudades = [0,0,0,0,0,0]
        pueblos= [0,0,0,0,0,0]
        jugActivo = [False,False,False,False]
        numDado = -1

        casilla = [self.clave,"",False,ciudades,pueblos,jugActivo,caminos,numDado]
        self.clave = casilla
    #generador de las casillas de MineralRandom
    def GenerarMineral(self):

        global contM
        global contO
        global contT
        global contL
        global contR
        global contD
        numRandom = int(random()*6 + 1)
        if numRandom == 1 and contM > 0:
            self.clave[1] = "MADERA"
            contM -= 1
        elif numRandom == 2 and contO > 0:
            self.clave[1] = "OVEJA"
            contO -= 1
        elif numRandom == 3 and contT > 0:
            self.clave[1] = "TRIGO"
            contT -= 1
        elif numRandom == 4 and contL > 0:
            self.clave[1] = "LADRILLO"
            contL -= 1
        elif numRandom == 5 and contR > 0:
            self.clave[1] = "ROCA"
            contR -= 1
        elif numRandom == 6 and contD > 0:
            self.clave[1] = "DESIERTO"
            contD -= 1
        elif contM == 0 and contO == 0 and contT == 0 and contL == 0 and contR == 0 and contD == 0:
            pass
        else:
            return self.GenerarMineral()
    #localizar un nodo en especifico empezando desde la raiz
    def Localizador(self,nombreNodo,secuencia):
        nodo = self
        for i in secuencia:
            if i == 0:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.Sup
            elif i == 1:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.SupDer
            elif i == 2:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.InfDer
            elif i == 3:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.Inf
            elif i == 4:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.InfIzq
            elif i == 5:
                if nodo.clave[0] == nombreNodo:
                    return nodo
                else:
                    nodo = nodo.SupIzq
            else:
                pass
    #introducir un puente a un jugador entre dos casillas
    def insCamino(self, num):
        numJug = int(input("\nIndica el numero de jugador: "))
        self.ModJugador(numJug)
        self.clave[6][num] = numJug
        if num == 0 and self.Sup != None:
            self.Sup.clave[6][3] = numJug
        elif num == 1 and self.SupDer != None:
            self.SupDer.clave[6][4] = numJug
        elif num == 2 and self.InfDer != None:
            self.InfDer.clave[6][5] = numJug
        elif num == 3 and self.Inf != None:
            self.Inf.clave[6][0] = numJug
        elif num == 4 and self.InfIzq != None:
            self.InfIzq.clave[6][1] = numJug
        elif num == 5 and self.SupIzq != None:
            self.SupIzq.clave[6][2] = numJug
        else:
            print("No se ha generado nodo espejo porque no existe")
            pass
    #Inserta una ciudad en la casilla especificada
    def insCiudad(self,num):
        numJug = int(input("\nIndica el numero de jugador: "))
        self.ModJugador(numJug)
        self.clave[3][num] = numJug
        if num == 0 and (self.SupDer != None or self.Sup != None):
            if self.Sup != None:
                self.Sup.clave[3][2] = numJug
                self.Sup.ModJugador(numJug)
            if self.SupDer != None:
                self.SupDer.clave[3][4] = numJug
                self.SupDer.ModJugador(numJug)
        elif num == 1 and (self.SupDer != None or self.Infder != None):
            if self.SupDer != None:
                self.SupDer.clave[3][3] = numJug
                self.SupDer.ModJugador(numJug)
            if self.InfDer != None:
                self.InfDer.clave[3][5] = numJug
                self.InfDer.ModJugador(numJug)
        elif num == 2 and (self.InfDer != None or self.Inf != None):
            if self.InfDer != None:
                self.InfDer.clave[3][4] = numJug
                self.InfDer.ModJugador(numJug)
            if self.Inf != None:
                self.Inf.clave[3][0] = numJug
                self.Inf.ModJugador(numJug)
        elif num == 3 and (self.Inf != None or self.InfIzq != None):
            if self.Inf != None:
                self.Inf.clave[3][5] = numJug
                self.Inf.ModJugador(numJug)
            if self.InfIzq != None:
                self.InfIzq.clave[3][1] = numJug
                self.InfIzq.ModJugador(numJug)
        elif num == 4 and (self.InfIzq != None or self.SupIzq != None):
            if self.InfIzq != None:
                self.InfIzq.clave[3][0] = numJug
                self.InfIzq.ModJugador(numJug)
            if self.SupIzq != None:
                self.SupIzq.clave[3][2] = numJug
                self.SupIzq.ModJugador(numJug)
        elif num == 5 and (self.SupIzq != None or self.Sup != None):
            if self.SupIzq != None:
                self.SupIzq.clave[3][1] = numJug
                self.SupIzq.ModJugador(numJug)
            if self.Sup != None:
                self.Sup.clave[3][3] = numJug
                self.Sup.ModJugador(numJug)
        else:
            print("No tiene nodos espejo")
            pass
    #Inserta un pueblo en la casilla identificada
    def insPueblo(self,num):
        numJug = int(input("\nIndica el numero de jugador: "))
        self.ModJugador(numJug)
        self.clave[4][num] = numJug
        if num == 0 and (self.SupDer != None or self.Sup != None):
            if self.Sup != None:
                self.Sup.clave[4][2] = numJug
                self.Sup.ModJugador(numJug)
            if self.SupDer != None:
                self.SupDer.clave[4][4] = numJug
                self.SupDer.ModJugador(numJug)
        elif num == 1 and (self.SupDer != None or self.Infder != None):
            if self.SupDer != None:
                self.SupDer.clave[4][3] = numJug
                self.SupDer.ModJugador(numJug)
            if self.InfDer != None:
                self.InfDer.clave[4][5] = numJug
                self.InfDer.ModJugador(numJug)
        elif num == 2 and (self.InfDer != None or self.Inf != None):
            if self.InfDer != None:
                self.InfDer.clave[4][4] = numJug
                self.InfDer.ModJugador(numJug)
            if self.Inf != None:
                self.Inf.clave[4][0] = numJug
                self.Inf.ModJugador(numJug)
        elif num == 3 and (self.Inf != None or self.InfIzq != None):
            if self.Inf != None:
                self.Inf.clave[4][5] = numJug
                self.Inf.ModJugador(numJug)
            if self.InfIzq != None:
                self.InfIzq.clave[4][1] = numJug
                self.InfIzq.ModJugador(numJug)
        elif num == 4 and (self.InfIzq != None or self.SupIzq != None):
            if self.InfIzq != None:
                self.InfIzq.clave[4][0] = numJug
                self.InfIzq.ModJugador(numJug)
            if self.SupIzq != None:
                self.SupIzq.clave[4][2] = numJug
                self.SupIzq.ModJugador(numJug)
        elif num == 5 and (self.SupIzq != None or self.Sup != None):
            if self.SupIzq != None:
                self.SupIzq.clave[4][1] = numJug
                self.SupIzq.ModJugador(numJug)
            if self.Sup != None:
                self.Sup.clave[4][3] = numJug
                self.Sup.ModJugador(numJug)
        else:
            print("No tiene nodos espejo")
            pass
    #inserta las casillas del tablero y lo crea
    def InsertarTablero(self,secuencia):
        nodo = self
        nodo.GenerarMineral()
        print("\nGenerando casillas del catan...")
        nodo.impNodo()
        for i in secuencia:
            print("")
            if i == 0:
                nodo.Sup.InsLista()
                nodo.Sup.GenerarMineral()
                nodo = nodo.Sup
                nodo.impNodo()
            elif i == 1:
                nodo.SupDer.InsLista()
                nodo.SupDer.GenerarMineral()
                nodo = nodo.SupDer
                nodo.impNodo()
            elif i == 2:
                nodo.InfDer.InsLista()
                nodo.InfDer.GenerarMineral()
                nodo = nodo.InfDer
                nodo.impNodo()
            elif i == 3:
                nodo.Inf.InsLista()
                nodo.Inf.GenerarMineral()
                nodo = nodo.Inf
                nodo.impNodo()
            elif i == 4:
                nodo.InfIzq.InsLista()
                nodo.InfIzq.GenerarMineral()
                nodo = nodo.InfIzq
                nodo.impNodo()
            elif i == 5:
                nodo.SupIzq.InsLista()
                nodo.SupIzq.GenerarMineral()
                nodo = nodo.SupIzq
                nodo.impNodo()
            else:
                pass
    #definir el numero de caida de dado que va a tener cada casilla
    def CasillaDado (self, secuencia):
        nodo = self
        secCont = 0
        global secDados
        nodo.clave[7] = secDados[secCont]
        secCont += 1
        print("\nGenerando numeros de las casillas...")
        nodo.impNodo()
        for i in secuencia:
            print("")
            if i == 0:
                if nodo.Sup.clave[1] == "DESIERTO":
                    nodo.Sup.clave[7] = -1
                    nodo = nodo.Sup
                    nodo.impNodo()
                else:
                    nodo.Sup.clave[7] = secDados[secCont]
                    nodo = nodo.Sup
                    secCont += 1
                    nodo.impNodo()
            elif i == 1:
                if nodo.SupDer.clave[1] == "DESIERTO":
                    nodo.SupDer.clave[7] = -1
                    nodo = nodo.SupDer
                    nodo.impNodo()
                else:
                    nodo.SupDer.clave[7] = secDados[secCont]
                    nodo = nodo.SupDer
                    secCont += 1
                    nodo.impNodo()
            elif i == 2:
                if nodo.InfDer.clave[1] == "DESIERTO":
                    nodo.InfDer.clave[7] = -1
                    nodo = nodo.InfDer
                    nodo.impNodo()
                else:
                    nodo.InfDer.clave[7] = secDados[secCont]
                    nodo = nodo.InfDer
                    secCont += 1
                    nodo.impNodo()
            elif i == 3:
                if nodo.Inf.clave[1] == "DESIERTO":
                    nodo.Inf.clave[7] = -1
                    nodo = nodo.Inf
                    nodo.impNodo()
                else:
                    nodo.Inf.clave[7] = secDados[secCont]
                    nodo = nodo.Inf
                    secCont += 1
                    nodo.impNodo()
            elif i == 4:
                if nodo.InfIzq.clave[1] == "DESIERTO":
                    nodo.InfIzq.clave[7] = -1
                    nodo = nodo.InfIzq
                    nodo.impNodo()
                else:
                    nodo.InfIzq.clave[7] = secDados[secCont]
                    nodo = nodo.InfIzq
                    secCont += 1
                    nodo.impNodo()
            elif i == 5:
                if nodo.SupIzq.clave[1] == "DESIERTO":
                    nodo.SupIzq.clave[7] = -1
                    nodo = nodo.SupIzq
                    nodo.impNodo()
                else:
                    nodo.SupIzq.clave[7] = secDados[secCont]
                    nodo = nodo.SupIzq
                    secCont += 1
                    nodo.impNodo()
            else:
                pass
    #modifica el nodo casilla del jugador que insertes a true es decir, indica que hay un jugador en la casilla
    def ModJugador(self,num):
            self.clave[5][num] = True
    #imprime un nodo de nuestra eleccion
    def impNodo(self):
        for i in self.clave:
            print(i,end=" ")


#----------------CREACION NODO RAIZ -----------------------------
root = Tablero("RAIZ")
root.InsLista()
#----------------CREACION CIRCULO CENTRAL -----------------------------
A1 = Tablero("A1")
B1 = Tablero("B1")
C1 = Tablero("C1")
D1 = Tablero("D1")
E1 = Tablero("E1")
F1 = Tablero("F1")
#----------------CREACION CIRCULO EXTERIOR -----------------------------
A2 = Tablero("A2")
B2 = Tablero("B2")
C2 = Tablero("C2")
D2 = Tablero("D2")
E2 = Tablero("E2")
F2 = Tablero("F2")
G2 = Tablero("G2")
H2 = Tablero("H2")
I2 = Tablero("I2")
J2 = Tablero("J2")
K2 = Tablero("K2")
L2 = Tablero("L2")
#funcion para que se genere el mapa para jugar
def generacionMapa():
#----------------GENERADOR DE MAPA------------------------------------
    #print("generando mapa...")
    #print("Uniendo la raiz...")
    root.insSup(A1)
    root.insSupDer(B1)
    root.insInfDer(C1)
    root.insInf(D1)
    root.insInfIzq(E1)
    root.insSupIzq(F1)
    #print("\nUniendo nodo A1..")
    A1.insSup(A2)
    A1.insSupDer(B2)
    A1.insInfDer(B1)
    A1.insInf(root)
    A1.insInfIzq(F1)
    A1.insSupIzq(L2)
    #print("\nUniendo nodo B1..")
    B1.insSup(B2)
    B1.insSupDer(C2)
    B1.insInfDer(D2)
    B1.insInf(C1)
    B1.insInfIzq(root)
    B1.insSupIzq(A1)
    #print("\nUniendo nodo C1..")
    C1.insSup(B1)
    C1.insSupDer(D2)
    C1.insInfDer(E1)
    C1.insInf(F2)
    C1.insInfIzq(D1)
    C1.insSupIzq(root)
    #print("\nUniendo nodo D1..")
    D1.insSup(root)
    D1.insSupDer(C1)
    D1.insInfDer(F2)
    D1.insInf(G2)
    D1.insInfIzq(H2)
    D1.insSupIzq(E1)
    #print("\nUniendo nodo E1..")
    E1.insSup(F1)
    E1.insSupDer(root)
    E1.insInfDer(D1)
    E1.insInf(H2)
    E1.insInfIzq(I2)
    E1.insSupIzq(J2)
    #print("\nUniendo nodo F1..")
    F1.insSup(L2)
    F1.insSupDer(A1)
    F1.insInfDer(root)
    F1.insInf(E1)
    F1.insInfIzq(J2)
    F1.insSupIzq(K2)
    #print("\nUniendo nodo A2..")
    A2.insInfDer(B2)
    A2.insInf(A1)
    A2.insInfIzq(L2)
    #print("\nUniendo nodo B2..")
    B2.insInfDer(C2)
    B2.insInf(B2)
    B2.insInfIzq(A1)
    B2.insSupIzq(A2)
    #print("\nUniendo nodo C2..")
    C2.insInf(D2)
    C2.insInfIzq(B1)
    C2.insSupIzq(B2)
    #print("\nUniendo nodo D2..")
    D2.insSup(C2)
    D2.insInf(E2)
    D2.insInfIzq(C1)
    D2.insSupIzq(B1)
    #print("\nUniendo nodo E2..")
    E2.insSup(D2)
    E2.insInfIzq(F2)
    E2.insSupIzq(C1)
    #print("\nUniendo nodo F2..")
    F2.insSup(C1)
    F2.insSupDer(E2)
    F2.insInfIzq(G2)
    F2.insSupIzq(D1)
    #print("\nUniendo nodo G2..")
    G2.insSup(D1)
    G2.insSupDer(F2)
    G2.insSupIzq(H2)
    #print("\nUniendo nodo H2..")
    H2.insSup(E1)
    H2.insSupDer(D1)
    H2.insInfDer(G2)
    H2.insSupIzq(I2)
    #print("\nUniendo nodo I2..")
    I2.insSup(J2)
    I2.insSupDer(E1)
    I2.insInfDer(H2)
    #print("\nUniendo nodo J2..")
    J2.insSup(K2)
    J2.insSupDer(F1)
    J2.insInfDer(E1)
    J2.insInf(I2)
    #print("\nUniendo nodo K2..")
    K2.insSupDer(L2)
    K2.insInfDer(F1)
    K2.insInf(J2)
    print("Tablero Generado...")
    root.InsertarTablero(secComandos)
#funcion para generar el colocador de numeros en cada casilla con orden correspondiente
def generacionCasillaDado():
    ok = False
    while ok == False:
        respuesta = str(input("Elige una esquina para comenzar ([A2] [K2] [I2] [G2] [E2] [C2]): "))
        if respuesta.upper() == "A2":
            A2.CasillaDado(secA2)
            ok = True
        elif respuesta.upper() == "K2":
            K2.CasillaDado(secK2)
            ok = True
        elif respuesta.upper() == "I2":
            I2.CasillaDado(secI2)
            ok = True
        elif respuesta.upper() == "G2":
            G2.CasillaDado(secG2)
            ok = True
        elif respuesta.upper() == "E2":
            E2.CasillaDado(secE2)
            ok = True
        elif respuesta.upper() == "C2":
            C2.CasillaDado(secC2)
            ok = True
        else:
            pass

#--------------------------COMIENZO DE PROGRAMA-------------------------------
generacionMapa()
print("")
generacionCasillaDado()
