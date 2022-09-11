#Mario Alexander Hernandez Quevedo
#Jonathan Roberto Acosta Lopez

import edad #Aca se hacen las impostaciones de donde tenemos el codigo para calcular la edad
import DUI_F#En esta linea se hacen las importaciones de donde tenemos le codigo para verificar si el usuario inserto el DUI correctamente o no

print("=============Bienvenido al sistema=============")

print("Ingrese uno de estos numero dependiendo de la accion que desea realizar: 1) Calcular edad .2) Ingresar DUI ")
menu = int(input())#Se toma el numero ingresado por el usuario


if menu == 1: #Si el usuario ingreso 1 se realizara esta accion
    calculo = edad.edad()
    print(calculo)

elif menu == 2:#Si el usuario ingreso el numero 2 el codigo realizara esta accion
    calculo_f = DUI_F.DUI()
    print(calculo_f)

else:
    print("NUMERO INGRESADO NO VALIDO, FAVOR DE INGRESAR ENTRE 1 Y 2")#Si el usuario intenta insertar un numero que no sea 1 o 2 se le avisara
    


