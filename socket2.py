while True:
    data = mysock.recv(512)  # Receive data in 512-byte chunks
    if len(data) < 1:  # If no data is received, exit the loop
        break
    mystring = data.decode()  # Decode the received data
    print(mystring)  # Print the decoded string


