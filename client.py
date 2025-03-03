import socket

HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"surya\n")
    s.sendall(b"03-03-2025\n")
    
    data = s.recv(1024).decode()  

print("Received:")
print(data)  
