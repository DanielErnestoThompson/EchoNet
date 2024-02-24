import socket

# Validate the user input to ensure it's a valid request.
def validate_request(request):
    valid_requests = ['get_time', 'echo', 'calculate_sum', 'get_uptime', 'get_active_users']
    return any(request.startswith(valid_cmd) for valid_cmd in valid_requests)


# Start the client and handle user input.
def start_client(host_ip, host_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_ip, host_port))
        print("Connected to the server. Type your requests (or type 'exit' to quit):")

        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break

            if validate_request(user_input):
                s.sendall(user_input.encode())
                data = s.recv(1024)
                print(f"Received: {data.decode()}")
            else:
                print("Invalid request format. Please try again.")


# Get server IP and port from user and initiate client connection.
if __name__ == "__main__":
    server_ip = input("Enter server IP: ")
    server_port = int(input("Enter server port: "))

    # Ensure there are two blank lines above according to PEP 8
    start_client(server_ip, server_port)
