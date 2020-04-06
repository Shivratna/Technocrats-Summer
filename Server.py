import socket
data =list()

#Creation:
s = socket.socket()          
port = 1241
cp=[]
j=0
c={}
addr={}

#Binding and connection:
s.bind(('', port))         
s.listen(5)      
for i in range(0,3):
    co, ao = s.accept()
    s.setblocking(1)
    c[co]='false'
    cp.append(co)
    addr[i]=0
    print(ao)
#Data Input:
n=int(input("Enter number of input : "))
for i in range(n):
    data.append(input())
i=0
print(data)
f=open("Output.txt","w")
#Main Process:
while data:
   msg=data.pop(0)
   j+=1
   for i in range(3):
       if addr[i]==0 and c[cp[i]]=='true':
           c[cp[i]]='false'
       if(c[cp[i]]=='false'):
           print(i+1)
           cp[i].send(msg.encode('utf-8'))
           cp[i].send(c[cp[i]].encode('utf-8'))
           c[cp[i]]='true';
           a=cp[i].recv(1024).decode('utf-8')
           b=cp[i].recv(1024).decode('utf-8')
           f.write(b) 
           addr[i]=int(a);
           break
   if j==3:
       x=min(addr.values())
       for i in range(3):
           addr[i]-=x
           print(addr[i])
       j-=1 
   print(msg)      
for i in range(3):
    cp[i].close()
f.close()
   #print(c.rec5v(1024).decode('ascii'))
