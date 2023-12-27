import socket

def start_server():
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 6254))
        s.listen()
        print("Server is listening....")
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received Message: {data.decode()}")

if __name__ == "__main__":
    start_server()


import socket

def start_server():
    with socket.socket(scoket.AF_INET, socket.SOCK_STREAM):
        s.bind(('127.0.0.1', 6254))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
