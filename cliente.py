import socket

host = 'localhost'  # Cambia esto por la dirección IP del servidor si corresponde
port = 7159  # Puerto en el que el servidor está escuchando

# Crea un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket al servidor remoto
client_socket.connect((host, port))

# Envía datos al servidor
message = input('Ingrese el mensaje: ')  # Permite al usuario ingresar el mensaje por consola
client_socket.sendall(message.encode())

# Recibe la respuesta del servidor
data = client_socket.recv(1024).decode()
print('Respuesta del servidor:', data)

# Cierra la conexión
client_socket.close()