import re


def find_address(equipment_number=""):
    '''
    文本内查找设备对应的地址
    '''
    target = open("log.txt")
    replace_symbol = re.sub("\n", "&", target.read())
    location = re.findall(equipment_number + ".*?&&", replace_symbol)
    result = re.findall("address is (\w{4}\.\w{4}\.\w{4})", location[0])
    print(result)
    target.close()

find_address("Loopback1")
