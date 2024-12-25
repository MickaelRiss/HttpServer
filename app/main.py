import socket  # noqa: F401

def handle_request(client_socket):
    # Read the request
    request = client_socket.recv(1024)
    print('Client request: ', request)
    # Send a response
    client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Starting server...")
    
    while True:
        #Wait for a connection
        print("Waiting for connection...")
        server_socket.listen()
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        handle_request(client_socket)
    
    server_socket.close()
    print("Server closed.")


if __name__ == "__main__":
    main()
