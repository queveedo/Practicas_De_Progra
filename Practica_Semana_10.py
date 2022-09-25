#Integarntes: Mario Alexander Hernandez Quevedo
#             Jonathan Roberto Acosta Lopez
#Importancion de tkinter
from tkinter import PhotoImage, Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox

def imprimir():
    #Obtener informacion de los widgets
    #Obteniendo el valor de los raddiobutton
    valor = float(input1.get())
    #Obteniendo el valor del input
    txt= float(input2.get())
    precio= valor * txt
    valor = int(radio.get())
    texto = "El precio es: $"

    #Se crea un if para evaluar si pagara con tarjeta o efectivo
    if valor == 1:
      precio1= precio * 0.2
      final = precio - precio1
      x = " Con un descuento de 20%"

    elif valor == 2:
        final = precio
        x = " Sin descuento"
    
    final_f = str(final)
   #Se le muestra un mensaje al usuario de cuanto debe pagar y si tendra descuento o no
    messagebox.showinfo(title="Cantidad a pagar", message=str(texto)+final_f+str(x))


#Se crea la ventana por medio del import que hicimos
vent1= Tk()
#Se ponen las dimensiones que tendra la ventana 
vent1.geometry("600x400")


radio = IntVar()

labl1=Label(vent1, bg = "#A5F3F3",text="INGRESE LA CANTIDAD DE PRODUCTOS")
input1=Entry(vent1)
labl2=Label(vent1,bg = "#A5F3F3", text="INGRESE EL PRECIO DE PRODUCTOS")
input2=Entry(vent1)



#Declaracion de los radio button
rdb1 = Radiobutton(vent1, bg = "#A5F3F3",text="Con tarjeta", value=1, variable=radio)
rdb2 = Radiobutton(vent1, bg = "#A5F3F3",text="Con efectivo", value=2, variable=radio)

btn1 = Button(vent1,bg="#A5F3F3",text="Calcular",command=imprimir)


#Mapeo de widgets
#se agrega color a la ventana
vent1.configure(bg='#D5F1F1')
#Se agrega titulo a la ventana
vent1.title("Cajero de Super mercado")
labl1.pack(pady=15)
input1.pack(pady=15)
labl2.pack(pady=15)
input2.pack(pady=15)
btn1.pack(pady=15)
rdb1.pack(pady=15)
rdb2.pack(pady=15)


vent1.mainloop()