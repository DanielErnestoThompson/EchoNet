import socket
from datetime import datetime
import time

# Global variables to track server uptime and active user count
start_time = time.time()
active_users = 0

def handle_request(request_type, message):
    # Handling different types of requests
    if request_type == 'get_time':
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif request_type == 'echo':
        return message
    elif request_type == 'calculate_sum':
        numbers = map(int, message.split(','))
        return str(sum(numbers))
    elif request_type == 'get_uptime':
        uptime_seconds = int(time.time() - start_time)
        return f"Server Uptime: {uptime_seconds} seconds"
    elif request_type == 'get_active_users':
        return f"Active Users: {active_users}"
    else: 
        return 'Unknown request type'

def start_server():
    global active_users
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 6254))
        s.listen()
        print('Server is listening....')
        while True:
            conn, addr = s.accept()
            with conn:
                active_users += 1  # Increment active user count
                print(f'Connected by {addr}')
                try:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        request_type, message = data.decode().split(':', 1)
                        response = handle_request(request_type, message)
                        conn.sendall(response.encode())
                except ValueError:
                    conn.sendall('Invalid request format'.encode())
                finally:
                    active_users -= 1  # Decrement active user count when a connection is closed
                    print(f'Disconnected from {addr}')

if __name__ == '__main__':
    start_server()
