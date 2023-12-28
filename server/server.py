import socket
from datetime import datetime

def handle_request():
    if request_type == 'get_time':
        return (datetime.now())
    elif request_type == 'echo':
        return message
    elif request_type == 'calculate_sum':
        numbers = map(int, message.split(','))
        return str(sum(numbers))
    else: 
        return 'Uknown request type'

def start_server():
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 6254))
        s.listen()
        print('Server is listening....')
        conn, addr = s.accept()
        with conn:
            print(f'Connected to {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                request_type, message = data.decode().split(':',1)
                response = handle_request(request_type, message)
                conn.sendall(response.encode())
if __name__ == '__main__':
    start_server()