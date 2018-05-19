# generador de mazo sin estados #
# -*- coding:utf-8 -*- #

from random import *


def pintasR():#Establece las pintas disponibles#
    return ["DIAMANTE","CORAZON"]

def pintasN():#Establece las pintas disponibles#
    return ["PICA","TREBOL"]

def nombres():#Establece los nombres disponibles#
    return ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

def mazo(pinta,nombre):#Crea el mazo de cartas#
    return [(x,y) for x in pinta for y in nombre]

def revolver(mazo): #Revuelve el mazo de cartas que tenemos# 
    return sample(mazo,len(mazo))

def pide_carta(mano,mazo): #Pide una carta al dealer#
    mano.append(mazo[0])
    return mazo[1:]

def valor_carta(carta,suma): #Da un valor a la carta segun su nombre#
    if carta[1] == 'J':
        return 10
    elif carta[1] == 'Q':
        return 10
    elif carta[1] == 'K':
        return 10
    elif carta[1] == 'A':
        if suma>10:
            return 1
        else:
            return 11
    else:
        return int(carta[1])

def sumar_cartas(mano): #Toma cada carta y suma su valor#
    if mano == []:
        return 0
    else:
        return valor_carta(mano[0]) + sumar_cartas(mano[1:])

def ver_mano_player(mano): #Imprime las cartas del jugador#
    print("\n Tienes estas cartas: "+ str(mano))

def ver_mano_casa(mano): #Imprime las cartas del dealer#
    print("\n La casa tiene: "+str(mano[0])+" y "+str("***Carta sin destapar***"))

def ver_mano_casa_final(mano):#Imprime las cartas finales de la casa#
    print("\n La casa tenia: "+str(mano))

def repartir(mazo,dealer,player): #Reparte las cartas al principio de la partida#
    player.append(mazo[0])
    player.append(mazo[1])
    dealer.append(mazo[2])
    dealer.append(mazo[3])
    return mazo[4:]
  
def sumar_mano(mano,suma):
    if mano ==[]:
        return suma
    else:
        for x in mano:
            return sumar_mano(mano[1:],suma+valor_carta(x,suma))


def suma_pintas(mano):
    if mano == []:
        return 0
    if mano[0][0] in pintasR():
        return 1 + suma_pintas(mano[1:])
    return suma_pintas(mano[1:])
    

def jugar(mazo,jugador,casa,estado,turno,suma,sumacom): #Empieza el juego de verdad#

    if  turno == 0 and estado == 0: #Empezar la partida revolviendo el mazo#
        jugar((revolver(mazo)),jugador,casa,estado+1,turno,suma,sumacom)
    elif turno == 0 and estado == 1: #Repartiendo las cartas#
        jugar(repartir(mazo,casa,jugador),jugador,casa,estado+1,turno,suma,sumacom)
    elif turno == 0:
        print("\n_______________________________________________________\n Tu turno comienza...")
        ver_mano_player(jugador)
        print("\n Tienes: "+str(sumar_mano(jugador,suma)))
        ver_mano_casa(casa)
                
        if sumar_mano(jugador,suma) >21:
            print("\n La casa GANA")
            ver_mano_casa_final(casa)
            return False
        
        elif sumar_mano(jugador,suma) == 21 and sumar_mano(casa,suma)>21:
            print("\n El jugador GANA")
            ver_mano_casa_final(casa)
            return True


    
        else:
            print("\n ¿Pides otra carta?")
            print("  SI/NO (S/N): ")
            if input()== 'S':
                jugar(pide_carta(jugador,mazo),jugador,casa,estado+1,turno,suma,sumacom)
            else: #Aqui empieza a jugar la maquina#
                jugar(mazo,jugador,casa,0,turno+1,suma,sumacom)

                
    if turno == 1: #Empieza el turno de la maquina#
        print("\n El turno de la maquina comienza...")
        ver_mano_player(jugador)
        print("\n Tienes:"+str(sumar_mano(jugador,suma)))
        ver_mano_casa(casa)
        print ("\n La casa tiene:"+str(sumar_mano(casa,sumacom)))
        if sumar_mano(casa,sumacom)<(sumar_mano(jugador,sumacom)):
          jugar(pide_carta(casa,mazo),jugador,casa,0,turno,suma,sumacom)
        else:
            if sumar_mano(jugador,suma) == sumar_mano(casa,suma):
                if suma_pintas(jugador) > suma_pintas(casa):
                    print ("\n El Jugador GANA")
                else:
                    print ("\n La casa GANA")
                ver_mano_casa_final(casa)
                return True
                    
            if sumar_mano(jugador,suma)<sumar_mano(casa,sumacom) and sumar_mano(casa,sumacom)<=21:
              print("\n La casa GANA")
              ver_mano_casa_final(casa)
              print ("\n fin del juego")
              return True
            else:
              print("\n Has Ganado")
              ver_mano_casa_final(casa)
              print ("\n fin del juego___________________________________________\n")
              return True
    

if __name__ == "__main__":
    print("    Este es el juego 21\n")

    while True:
      jugar(mazo(pintasR()+pintasN(),nombres()),[],[],0,0,0,0)
