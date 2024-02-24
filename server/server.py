import socket
from datetime import datetime
import time
import threading

# Global variables to track server uptime and active user count
start_time = time.time()
active_users = 0
active_users_lock = threading.Lock()


def handle_request(request_type, message):
    if request_type == 'get_time':
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif request_type == 'echo':
        return message
    elif request_type == 'calculate_sum':
        try:
            numbers = map(int, message.split(','))
            return str(sum(numbers))
        except ValueError:
            return "Error: Invalid numbers for calculation."
    elif request_type == 'get_uptime':
        uptime_seconds = int(time.time() - start_time)
        return f"Server Uptime: {uptime_seconds} seconds"
    elif request_type == 'get_active_users':
        with active_users_lock:
            return f"Active Users: {active_users}"
    else:
        return 'Unknown request type'


def handle_client(conn, addr):
    global active_users
    with active_users_lock:
        active_users += 1
    print(f'Connected by {addr}')
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                request_type, message = data.decode().split(':', 1)
            except ValueError:
                request_type, message = data.decode(), ''
            response = handle_request(request_type, message)
            conn.sendall(response.encode())
    finally:
        with active_users_lock:
            active_users -= 1
        conn.close()
        print(f'Disconnected from {addr}')


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 6254))
        s.listen()
        print('Server is listening....')
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()


if __name__ == '__main__':
    start_server()
