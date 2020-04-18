# 练习:英文语句，按照单词进行翻转.
# How are you  -->  you are How

message = "How are you"
list_message = message.split(" ")
# list_message.reverse()# 没有创建新空间，在原有空间的翻转
# message = " ".join(list_message)
message = " ".join(list_message[::-1])
print(message)


#mywork version1
sentence="how are you"
list1=sentence.split(" ")
list1.reverse()
message=" ".join(list1)
print(message)

#mywork version2
sentence="how are you"
list1=sentence.split(" ")
message=" ".join(list1[::-1])
print(message)

