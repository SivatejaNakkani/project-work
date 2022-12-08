import socket
class AddressingRoutingProtocolClient:

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("localhost",1234))
    a = input("ARP OR RARP :")
    if(a=='ARP'):
        add=input("Enter IP:")
    else:
        add=input("Enter MAC:")
    s.send(add.encode())
    mac = s.recv(1024)
    mac=mac.decode("utf-8")
    #if("a==ARP"):
    print('MAC OF',add,'is:',mac)
    #else:
        #print('IP of ',add,'is:',mac)
       

connection = AddressingRoutingProtocolClient
connection()
