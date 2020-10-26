import socket
import threading
import os

HEADER = 64  #64 bytes -> Representa el tamaño de bytes del mensaje que vamos a recibir
PORT = 5050
#SERVER = "192.168.1.50"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "QUIT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "HELO":
                conn.send("100 OK".encode(FORMAT))
            elif msg == "LIST":
                strfiles = ""
                for x in os.listdir('.'):
                    strfiles+=x+"\n"
                conn.send(strfiles[:-1].encode(FORMAT))  
            elif msg[0:5] == "NBUCK":
                dirname = msg.strip("NBUCK")
                try:
                    os.mkdir(dirname)
                except OSError:
                    conn.send("Creation of the directory failed".encode(FORMAT))
                else:
                    conn.send("Successfully created the directory".encode(FORMAT))
            elif msg[0:6] == "DLBUCK":
                dirname = msg.strip("DLBUCK")
                try:
                    os.rmdir(dirname)
                except OSError:
                    conn.send("Directory deletion Failed".encode(FORMAT))
                else:
                    conn.send("Directory successfully deleted".encode(FORMAT))  
            elif msg[0:2] == "CD":
                chdirname = msg.strip("CD")
                try:
                    os.chdir(chdirname)
                    conn.send("Directory changed".encode(FORMAT))
                except OSError:
                    conn.send("Can't change the Current Working Directory".encode(FORMAT))
            elif msg[0:6] == "UPFILE":
                filenameaux1 = msg.strip("UPFILE")
                filenameaux = filenameaux1.split(".,")
                filename = filenameaux[0]
                content = filenameaux[1]
                try:
                    f = open(filename,"w")
                    f.write(content)
                    f.close()
                    conn.send("File successfully uploaded".encode(FORMAT))
                except:
                    conn.send("File failed to upload".encode(FORMAT))
            elif msg == "BK":
                try:
                    os.chdir("../")
                    conn.send("You went back from directory".encode(FORMAT))
                except OSError:
                    conn.send("Can't go back from directory".encode(FORMAT))        
            elif msg[0:4] == "DATA":
                msg = msg.strip("DATA")
                f = open("msg_storage.txt","a")
                f.write(msg+"\n")
                f.close()
                conn.send("300 DRCV".encode(FORMAT))
            else:
                conn.send("400 BCMD\nCommand-Description: Bad command".encode(FORMAT))

            print(f"[{addr}] {msg}")

    print(f"[SERVER][{addr}] Disconnected from the server")
    conn.close()
    
    
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting")
start()