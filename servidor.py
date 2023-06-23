import socket

host = 'localhost'  # Dirección IP en la que el servidor escucha todas las interfaces de red
port = 7159  # Puerto en el que el servidor escucha

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asocia el socket al host y al puerto
server_socket.bind((host, port))

# Escucha conexiones entrantes
server_socket.listen(1)

print('Servidor escuchando en', host, 'puerto', port)

while True:
    # Espera por una nueva conexión
    print('Esperando por una conexión...')
    client_socket, client_address = server_socket.accept()
    print('Conexión establecida desde', client_address)

    # Recibe los datos del cliente
    data = client_socket.recv(1024).decode()
    print('Datos recibidos:', data)

    # Envía una respuesta al cliente
    response = '¡Hola, cliente!'
    client_socket.sendall(response.encode())

    # Cierra la conexión con el cliente
    client_socket.close()
