import socket

HEADER = 64  #64 bytes -> Representa el tamaño de bytes del mensaje que vamos a recibir
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "quit"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) #Completar los 64 bytes
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def start():
    print("Welcome to the server, 'HELP' to see the available commands")
    while True:
        msg = input()
        
        if msg == "DATA":
            msg_data = input("Input data to send: ")
            send("DATA"+msg_data)
        elif msg == "HELP":
            print("quit, DATA, HELO, NBUCK, DLBUCK, UPFILE, DNFILE DLFILE, SLIST, CLIST, CD, BK")
        elif msg == "NBUCK":
            msg_nbuck = input("Name the bucket: ")
            send("NBUCK"+msg_nbuck)
        elif msg == "DLBUCK":
            msg_dlbuck = input("Name of the bucket: ")
            send("DLBUCK"+msg_dlbuck)
        elif msg == "CD":
            msg_cdbuck = input("Name of the bucket: ")
            send("CD"+msg_cdbuck)
        elif msg == "UPFILE":
            filename = input("Name of the file to upload: ")
            f = open(filename,"r")
            content = f.read()
            send("UPFILE"+filename+".,"+content)
            f.close()
        elif msg == "DLFILE":
            print("hola")
        elif msg == "LIST":
            print("hola")                                                               
        elif msg == "quit":
            send(msg)
            print("Disconnected from the server")
            break
        else:
            send(msg)

start()