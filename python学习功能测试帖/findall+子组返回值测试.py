"""
re模块演示1
"""
import re

# print(re.findall('abab',"ababababab"))
# print(re.findall('(ab)ab',"ababababab"))
print(re.match('(ab)(ab)',"ababababab").group(0))
