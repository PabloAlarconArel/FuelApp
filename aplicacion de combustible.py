import socket
import io
from tkinter import *

#funcion para obtener datos de el servidor.
def dato():
    while(True) :
        enchufe=socket.socket()
        enchufe.connect(('localhost',8000))
        respuesta=int(enchufe.recv(1024))
        z.set(respuesta)
        c.place(x=300,y=580,width=( respuesta*6),height=20)
        return respuesta
        c.after(1000,dato)
        
    enchufe.close()
      
def capacidad():
#funcion para observar la cantidad de gasolina que tiene el estanque.
    porcentaje= dato()

    estanque=Button(v,bg="white",width=250,height=200,)
    if(porcentaje >= 0 and porcentaje <= 33):
        vacio=PhotoImage(file="vacio.png")
        estanque.image= vacio
        estanque.config(image=vacio)
        estanque.place(x=1020,y=200)
    if(porcentaje >= 34 and porcentaje <= 66):
        medio=PhotoImage(file="medio.png")
        estanque.image= medio
        estanque.config(image= medio)
        estanque.place(x=1020,y=200)
    if(porcentaje >= 67 and porcentaje <= 100):
        lleno=PhotoImage(file="lleno.png")
        estanque.image= lleno
        estanque.config(image=lleno)
        estanque.place(x=1020,y=200)
    v.after(1000,capacidad)

def guardar ():
#funcion para guardar los datos del cliente hacia el servidor.
    datocliente= open("porcentajeDecombustible.txt","a+")
    cuenta=str(cajaCuen.get())
    datocliente.write("Numero de cuenta:  ")
    datocliente.write(cuenta)
    datocliente.write("\n")
    dinero=str(cajaDine.get())
    datocliente.write("Valor pagado:  $")
    datocliente.write(dinero)
    datocliente.write("\n")
    datocliente.close()
    ventana2()

def salir():
#comando destroy se utiliza para cerrar una ventana
    v.destroy()
    
    
def ventana0():
#ventana que solicita una contraseña de acceso
    global caja 
    global ventana
    ventana=Tk()    
    ventana.title("contraseña")
    ventana.geometry("500x500+500+200")
    txt=Label(ventana,text="ingrese la clave de acceso").pack()
    n=IntVar()
    caja=Entry(ventana,textvariable=n,show="*") 
    caja.place(x=200,y=50)
    boton=Button(ventana, text="ACEPTAR", width=10, height=3, command=ventana1)
    boton.place(x=200, y=250)
    
    ventana.mainloop()
def ventana1():
#ventana en la que se solicita los datos del cliente
    global v2
    global cajaCuen
    global cajaDine
    clave=0
    a=float(caja.get())
    if(a==clave):
        ventana.destroy()
        v2=Tk()
        v2.geometry("700x400+400+200")
        v2.title("SERVICIO")
        titulo=Label(v2,text="Bienvenido", font=("Verdana",25)).pack()    
        txt=Label(v2,text="N° de cuenta:").place(x=150,y=100)
        n1=IntVar()
        cajaCuen=Entry(v2,textvariable=n1)
        cajaCuen.place(x=300,y=100)    
        txto=Label(v2,text="Cuanto desea cargar:      $").place(x=150,y=150)
        n2=IntVar()
        cajaDine=Entry(v2,textvariable=n2)
        
        cajaDine.place(x=300,y=150)
        boton=Button(v2, text="Aceptar", width=10, height=3, command=guardar)
        boton.place(x=300, y=200)
    else:
#SE ABRE UNA VENTANA SI LA CONTRASEÑA ES INCORRECTA
        v4=Tk()
        v4.geometry("300x100+600+300")
        v4.title("ERROR")
        titulo=Label(v4,text="")
        titulo.pack()
        titulo=Label(v4,text="ingreso de manera incorrecta la contraseña")
        titulo.pack()
        titulo=Label(v4,text="intente nuevamente")
        titulo.pack()
        v4.mainloop()
    
    
def ventana2(): 
    global z
    global v
    global c
#ventana que muestra el abastecimiento del auto
#creacion de la ventana tkinter y respectivos label.
    v2.destroy()
    v=Tk()
    v.title("Combustible")
    v.geometry("1400x700+50+50")
    v.config(bg="#5EBC6E")
    titulo= Label(v,text="LLenado del estanque de combustible")
    titulo.config(fg="orange",bg="#505668",font=("bold italic",20))
    titulo.place(x=350,y=40)

#insertar imagen
    imagen= PhotoImage(file="automovil.png")
    foto=Label(v,image= imagen)
    foto.place(x=200,y=200)


#barra para insertar el cambio de combustible en el estanque
    barra=Label(v)
    barra.config(bg="white")
    barra.place(x=300,y=580,width=600,height=20)
    tporcentaje=Label(v,text="%")
    tporcentaje.place(x=905,y=580)
    tporcentaje.config(bg="black",fg="white",font=("helvetica",10))

#creacion de la barra de porcentaje del estanque.
    z=IntVar()
    c=Entry(v,textvariable=z)
    c.config(bg="orange",fg="white", font=("verdana",10))
    c.place(x=300,y=580,width=100,height=20)

#boton salir (cierra todo)
    boton=Button(v, text="Salir", width=10, height=3, command=salir)
    boton.place(x=1120,y=500)

    capacidad()
    
    v.after(1000,dato)

    v.mainloop()
 

ventana0()  
