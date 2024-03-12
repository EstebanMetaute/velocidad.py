import os

def fnt_limpiarpantalla():
    os.system('cls')
    print('cual es la velocidad del auto')
    print('\n\n')


def fnt_menu(repetir):
    while repetir == True:
        fnt_limpiarpantalla()
        opcionStr = input('\n1. velocidad\n ->')
        if opcionStr == 'F' or opcionStr == 'f':
            repetir = False
        else:
            if int(opcionStr) == 1:
                numero1Flt = float(input('ingrese distancia (km) ->'))
                numero2Flt = float(input('ingrese tiempo (hrs) ->'))
                fnt_operaciones(numero1Flt,numero2Flt,opcionStr)
            else:
                print('\nOpcion incorrecta')
                enter = input('\n<ENTER>')
            
    
def fnt_operaciones(n1,n2,op):
    
    if op == '1':
        if n2 == 0:
            enter = input('\nNo se puede dividir por 0 <ENTER>')
        else:
            resultadoFlt = n1 / n2
            operadorStr = '/'
    print('la velocidad claculada es: ', resultadoFlt, )
    enter = input('\n<ENTER>')

fnt_menu(True)