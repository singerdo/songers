import re
file = open("log.txt", "r")

device_name = input(">>")

list_log = re.split(r"\n{2}", file.read())

for item in list_log:
    if device_name in item:
        result = re.search(r"address is (?P<ip_address>(\w{4}\.){2}(\w{4}))", item).group()
        print(result)
        break
else:
    print("没有此设备")

file.close()