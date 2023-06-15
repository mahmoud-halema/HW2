import socket

# Define server address and port
HOST = 'localhost'
PORT = 8000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Get the calculation expression from the user
expression = input('Enter a calculation expression: ')

# Send the expression to the server
client_socket.send(expression.encode('utf-8'))

# Receive the result from the server
result = client_socket.recv(1024).decode('utf-8')

# Print the result
print(f'Result: {result}')

# Close the socket connection
client_socket.close()

