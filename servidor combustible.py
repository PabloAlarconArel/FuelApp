import socket
import io

#consumidor UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',2000))
#servidor TCP

s1=socket.socket()
s1.bind(('localhost',8000))

while(True) :
    data,addr=s.recvfrom(1024)
    s1.listen()
    conexion,addr = s1.accept()
    combustible= open("porcentajeDecombustible.txt","a+") #creacion de documento de texto
    porcentaje=str(data.decode())
    print(data.decode())
    combustible.write("la capacidad de combustible es: ")
    combustible.write(porcentaje)
    combustible.write("%")
    combustible.write("\n")
    combustible.close()
    print ('Conexion con dirreccion:', addr)
    conexion.send(data)
    conexion.close()

s.close()


