import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 6254))

        # Updated list of requests including new ones
        requests = [
            'get_time',
            'echo: Hello, Server!',
            'calculate_sum:5,3',
            'get_uptime',  # New request for server uptime
            'get_active_users'  # New request for active user count
        ]

        for req in requests:
            s.sendall(req.encode())
            data = s.recv(1024)
            print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_client()
