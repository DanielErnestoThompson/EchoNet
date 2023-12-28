import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 6254))

        # Testing new requests on server 
        requests = [
            'get_time',
            'echo: Hello, Server!',
            'calculate_sum:5,3'
        ]

        for req in requests:
            s.sendall(rec.encode())
            data = s.recv(1024)
            print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_client()