while true:
    data = mysock.recv(512)
    if (len(data)<1):
        break
        print(data.decode())

while True:  # Capitalize "True"
    data = mysock.recv(512)  # Receive up to 512 bytes from the socket
    if len(data) < 1:  # If no data is received, exit the loop
        break
    print(data.decode())  # Decode and print the data

mysock.close()  # Ensure this is outside the loop to close the socket
