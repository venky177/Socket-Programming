import socket
import threading

class sc(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        threadlock.acquire()
        ch=client.recv(1111)
        if ch=='1':
            f=open('temp.txt','a+')
            r=client.recv(4096)
            f.write(r+'\n')
            f.close()
        else:
            f=open('temp.txt','a+')
            msg=f.read()
            client.send(msg)
            f.close()
        threadlock.release()
threadlock=threading.Lock()
s=socket.socket()
s.bind(('127.0.0.1',5221))
s.listen(5)
for i in range (0,5):
    client,client_addr=s.accept()
    s1=sc()
    s1.start()
    s1.join()
client.close()
s.close()