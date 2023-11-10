import socket
from gtts import gTTS
import os
from unidecode import unidecode

# Define the server's address and port
server_address = ('', 12345)  # Use an empty string for the server address to bind to all available network interfaces

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)  # The argument specifies the maximum number of queued connections

print("Server is listening on port 12345...")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print("Received:", data.decode())
        text_without_marks = unidecode(data.decode()).replace(" ", "_")
        text_without_marks = text_without_marks.replace(".", "_")
        text_without_marks += ".mp3"
        current_directory_files = os.listdir()
        if text_without_marks not in current_directory_files:
            print("need to translate " + text_without_marks)
       	    tts = gTTS(text=data.decode(), lang='vi')
            tts.save(text_without_marks)

        # Play the recognized message
        os.system("sudo omxplayer --layer 2 -o local " + text_without_marks)
        # Send a response back to the client
        response = "Hello, client!"
        client_socket.sendall(response.encode())

    finally:
        # Close the client socket
        client_socket.close()
