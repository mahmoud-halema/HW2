import socket

# Define server address and port
HOST = 'localhost'
PORT = 8000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Define a function to handle incoming requests from clients
def handle_client(client_socket):
    # Receive the calculation expression from the client
    expression = client_socket.recv(1024).decode('utf-8')
    
    # Evaluate the expression and compute the result
    result = str(eval(expression))
    
    # Send the result back to the client
    client_socket.send(result.encode('utf-8'))

    # Close the socket connection
    client_socket.close()

# Main server loop
while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    print(f'Client connected from {client_address[0]}:{client_address[1]}')

    # Handle the client's request
    handle_client(client_socket)
