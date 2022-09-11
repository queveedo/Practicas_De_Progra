#Mario Alexander Hernandez Quevedo
#Jonathan Roberto Acosta Lopez




def edad():
        
        annio = input("Favor de ingresar tu año de nacimiento: ")#En esta linea se toma la fecha o el numero introducido que sera representado por el año en que nacio

        if annio.isdigit():#Aca se valida si ingreso 4 digitos, que son los digitos necesarios para ingresar un AÑO
            if len(annio)==4: #En esta linea validara si ingreso 4 digitos, si esto es asi ejecutara toda la linea de codigo que se encuentra en esta
                
                 edad = 2022 - float(annio)
                 if edad >= 18:
                    return("Usted es mayor de edad")
          
        
                 elif edad > 0:
                    return("Usted es menor de edad")
           
            else:
                print("EXCEDIO LOS DIGITOS QUE CONTIENE UN AÑO O INGRESO MENOS DIGITOS, FAVOR DE INGRESAR UN AÑO VALIDO ")#Se le avisa al usuario si el AÑO que ingreso tiene mas o menos digitos del que deberia tener

        else:
            print("INGRESO UNA LETRA O CARACTER, FAVOR DE INGRESAR UN AÑO VALIDO")#Se el avisa al usuario que lo ingreso fue una letra o algun tipo de caracter que no sea un AÑO

                


           
    


