import re

string = "hello,i am learning how to use Regex"

print('\n-----匹配字符串-----\n')
print(re.match(r'learn',string))    #只匹配开头
print(re.search(r'learn',string))   #全局搜索
print(re.findall(r'o',string))      #匹配所有，返回一个列表


print('\n-----先编译一个正则表达式，再进行匹配-----\n')
pattern = re.compile(r'learn')  #编译一个正则表达式
print(pattern.match(string))
print(pattern.search(string))

m = pattern.search(string)
print(m.span())        #返回一个元祖（开始，结束）的位置
print(m.group())       #返回正则匹配的字符串
print(m.start())       #返回匹配开始的位置(第一位从0开始)
print(m.end())         #返回匹配结束的位置

print('-----利用正则分隔字符串-----')
print(re.split(r'\s',string))           #按空格分隔，返回一个列表