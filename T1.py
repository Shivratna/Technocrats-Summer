#TRuck1
import socket                
import time

s = socket.socket()          
port = 1241          

s.connect(('127.0.0.1', port))
s.setblocking(1)

while True:
    dat = s.recv(1024).decode('utf-8')    
    t = dat.split(' ')
    loc = t[0]
    ti =int(t[1])
    
    con = s.recv(1024).decode('utf-8')
    if con=='false':
        s.send(t[1].encode('utf-8'))
        
    b=loc+' Truck1\n'
    print("Writing into file")
    s.send(b.encode('utf-8'))
    

