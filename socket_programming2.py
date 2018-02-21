import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()
print('Socket Created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit();

print ('Socket bind complete')


# Start listening on socket
s.listen(10)
print('Socket now listening')

# now keep talking with the client
conn, addr = s.accept()

print('Connected with ' + addr[0] + ':' + str(addr[1]))

# now keep talking with the client
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()