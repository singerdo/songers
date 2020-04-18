from socket import *

class ChatRoom():
    def __init__(self,list,addr=("127.0.0.1",8888)):
        self.addr=addr
        self.list=list

    def start(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(self.addr)
        dict_user={}
        list_keepout=[]
        while True:
            data,addr=s.recvfrom(1024)
            print("已链接：",addr)
            name = data.decode().split("$", 2)[1]
            if addr in list_keepout:
                continue

            elif data.decode().split("$",2)[0]=="N":
                a=0
                dict_user[name] = [addr,a]

            elif data.decode().split("$",2)[0]=="M":
                content=data.decode().split("$",2)[2]
                for word in self.list:
                    print(word)
                    if word in content:
                        dict_user[name][1] += 1
                        print(dict_user[name][1])
                        for i in dict_user.values():
                            message = "%s试图散步不良信息" % name
                            s.sendto(message.encode(), i[0])
                        break
                else:
                    for i in dict_user.values():
                        message="%s：%s"%(name,content)
                        s.sendto(message.encode(),i[0])

                if dict_user[name][1]==3:
                    list_keepout.append(addr)
                    del dict_user[name]
                    s.sendto("你发布不当信息已被拉入黑名单".encode(), addr)

            elif data.decode().split("$",2)[0]=="Q":
                del dict_user[name]
                for i in dict_user.values():
                    message="%s+退出聊天室" % name
                    s.sendto(message.encode(),i[0])

address=("127.0.0.1",8888)
list_forbiden = ["aa", "bb", "xx", "oo"]
a=ChatRoom(list_forbiden,address)
a.start()