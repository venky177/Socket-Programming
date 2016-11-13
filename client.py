import socket
c=socket.socket()

c.connect(("127.0.0.1",5221))
ch=raw_input("Enter choice: 1 Write  2 Read\n")
c.send(ch)
if ch=='1':
    print "Writing to the file...\n"
    msg=raw_input("-->")
    c.send(msg)
else:
    print("file contents are...\n")
    msg=c.recv(4096)
    print(msg)
c.close()

    