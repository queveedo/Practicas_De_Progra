#Mario Alexander Hernandez Quevedo
#Jonathan Roberto Acosta Lopez

def DUI():

     dui = input("Por favor ingresar su numero de DUI: ")# se toma el numero de DUI ingresado por el usuario

     if dui.isdigit():#Aca se valida si ingreso 9 digitos, que son los digitos totales que contiene un numero de DUI
        if len(dui)==9:#Si ingreso un total de 9 numeros o digitos en este caso se le dira al usuario que su numero de DUI esa valido
            print("NUMERO DE DUI VALIDO")
        else:
            print("NUMERO DE DUI INVALIDO, EXCEDIO LA CANTIDAD DE NUMEROS PERMITIDOS O INGRESO MENOS NUMEROS")#Se el avisa al usuario que excedio o puso menos digitos, por lo cual no puede ser un numero de DUI
     else:
        print("DUI INVALIDO, INGRESO LETRAS O CARACTER INVALIDO, FAVOR DE INGRESAR NUMEROS")#Se el avisa al usuario que ingreso algun tipo de letra o algun tipo de cararter que no es valido
        