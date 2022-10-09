
'''
Integrantes:Mario Alexander Hernandez Quevedo
            Jonatan Roberto Acosta Lopez
'''

#Se hacen las impostaciones que necesitaremos para esta practica
from cgitb import text
from operator import index
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import   Tk, Entry, Label, Button, messagebox
from turtle import st


#Creamos la ventana que presentaremos, le agregamos un titulo y le especificamos sus dimensiones
vent1= Tk()
vent1.geometry("720x380")
vent1.configure(bg='white')

vent1.title('SEND GMAIL')

#Creamos la funcion llamada enviar 
def Enviar():
   
   #Creamos las variables del correo remitente , correo destinatario y usuario
    correo_remitente = 'marioquevedo.spotify@gmail.com'
    correo_destinatario = (input1.get())
    usuario = (input2.get())
 
    # Creamos el mensaje como un objeto
    mensaje = MIMEMultipart()
     
    #Se crea el molde de como enviremos el msj tipo html
    mensaje_html="""
    <!DOCYPE html>
    <html>
    <body>
    <h1> Hello {}</h1>
    <p>{}</p>
    </body>
    </html>
    """
 
    #Aca establecemos los atributos del mensaje
   
    mensaje['From'] = correo_remitente
    mensaje['To'] = correo_destinatario
    mensaje['Subject'] = 'Mensaje Automatico'
    

    # En esta linea creamos el cuerpo del msj
    cuerpo = (input3.get())

    # Ya despuedes de haber hecho lo anterior lo agregamos al objeto mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(mensaje_html.format(usuario,cuerpo), 'html'))
    


    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
  

    sesion_smtp.starttls()
  
    #Agregamos nuestro correo o el correo remitente para iniciar sesion con el servidor
    sesion_smtp.login('marioquevedo.spotify@gmail.com','ocsbobgepiddenwu')

    # Convertimos el objeto que creamos anteriormente y lo pasamos a tipo string
    texto =  mensaje.as_string()

    # Aqui enviamos el gmail
    sesion_smtp.sendmail(correo_remitente, correo_destinatario, texto)
 
    # En este apartado cerramos la conexion
    sesion_smtp.quit()
    texto_f="The mail was sent correctly!!!"
    messagebox.showinfo(title="Enviar", message=str(texto_f))


#Se crean lops botones, los labels correspondientes y los Entry
labl1=Label(vent1, bg = "#f35454",text="Send To:")
input1=Entry(vent1)
labl2=Label(vent1,bg = "#f3e554", text="User name:")
input2=Entry(vent1)
labl3=Label(vent1, bg = "#7ff354",text="Message body:")
input3=Entry(vent1)
btn1 = Button(vent1,text="Send",command=Enviar,bg='#54abf3')

#En estas lineas de codigo definimos las posiciones de cada cosa que creamos anteriormente y que se muentren en pantalla
labl1.place(x=95, y=20)
input1.place(x=150, y=20)
labl2.place(x=80, y=60)
input2.place(x=150, y=60)
labl3.place(x=63, y=100)
input3.place(x=150, y=100, relwidth=0.5,relheight=0.4)
btn1.place(x=350, y=300)
vent1.mainloop()