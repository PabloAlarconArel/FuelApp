import socket
import random
import time

#consumidor UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):
    #la variable "dato" es el nivel de combustible del auto
    dato=int(random.randrange(0,50))
    #se modifica el nivel de combustible de manera ascendente
    while(dato<=100):
        dato1=dato
        dato1=str(dato1)
        dato2=dato1.encode()
        s.sendto(dato2,('localhost',2000))
        print(dato2)
        dato=int(dato1)
        dato=dato+1
        time.sleep(1)
