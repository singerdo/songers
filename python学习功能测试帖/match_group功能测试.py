
import re
a = "123abc456"
print (re.match("([0-9]*)[a-z]*[0-9]*",a).group())   #123abc456,返回整体
print (re.match("([0-9]*)([a-z]*)[0-9]*",a).group(1))   #123
print (re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print (re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(3))
