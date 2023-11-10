import socket

# Define the server's address and port
server_address = ('localhost', 12345)  # Replace with the actual server's address and port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hoang Cong Hung"
    client_socket.sendall(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())

finally:
    # Close the socket
    client_socket.close()
