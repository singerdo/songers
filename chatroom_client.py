from socket import *
from multiprocessing import Process

def send(s):

    name=input("请输入你的姓名：")
    data="N$"+name
    s.sendto(data.encode(),("127.0.0.1",8888))
    while True:
        content=input(">>")
        if content=="exit":
            data="Q$"+name
            s.sendto(data.encode(),("127.0.0.1",8888))
            break
        data="M$"+name+"$"+content

        s.sendto(data.encode(),("127.0.0.1",8888))

def receive(s):

    while True:
        answer,addr=s.recvfrom(1024)
        print(answer.decode()+"\nspeak:")

def main():

    s = socket(AF_INET, SOCK_DGRAM)
    p = Process(target=receive,args=(s,))
    p.start()
    send(s)
    p.join()

main()

