import socket

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysock.connect(('data.pr4e.org', 80))

# Prepare the GET request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Send the GET request
mysock.send(cmd)

# Receive and display the response
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

# Close the socket
mysock.close()




