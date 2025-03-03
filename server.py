import socket

HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
    except Exception as e:
        print(f"Error binding to {HOST}:{PORT}: {e}")
        exit()
    
    s.listen()
    print(f"Listening on {HOST}:{PORT}...")

    try:
        conn, addr = s.accept()
    except Exception as e:
        print(f"Error accepting  connection: {e}")
        exit()

    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            except Exception as e:
                print(f"Error receiving/sending data: {e}")
                exit()

