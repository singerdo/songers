"""
web server

提供一个服务端使用类,通过这个类可以快速的搭建一个web server服务,用以展示自己的简单网页
"""

from socket import *
from select import select

#　主体功能　
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,html=None):
        self.host = host
        self.port = port
        self.html = html
        # 创建套接字和地址绑定工作
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setblocking(False)

    def bind(self):
        self.address = (self.host,self.port)
        self.sockfd.bind(self.address)

    # 启动服务 准备接受链接的过程
    def start(self):
        self.sockfd.listen(3)
        print("Listen the port %s"%self.port)
        # select TCP并发服务
        self.sockfd.setblocking(False)
        rlist=[self.sockfd]
        wlist=[]
        xlist=[]
        while True:
            rs,ws,xs=select(rlist,wlist,xlist)
            for i in rs:
                if i is self.sockfd:
                    connfd,addr=i.accept()
                    connfd.setblocking(False)
                    print("已连接上：",addr)
                    rlist.append(connfd)
                else:
                    data=i.recv(2048).decode()
                    print("已收到消息",data)
                    http_data = """HTTP/1.1 200 OK
                    Content-Type:text/html
    
                    hello
                    """
                    i.send(http_data.encode())









if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务
    static中有一组网页,我为了展示我的这组网页
    """

    # 需要使用者提供 : 网络地址   网页位置
    host = "0.0.0.0"
    port = 8000
    dir = "./static"

    # 实例化对象
    httpd = HTTPServer(host=host,port=port,html=dir)

    # 调用方法启动服务
    httpd.start()

