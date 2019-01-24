import re

string = '''<a href="https://www.lagou.com/zhaopin/Java/" data-lg-tj-id="4A00" data-lg-tj-no="0001" data-lg-tj-cid="idnull">Java</a>
            <a href="https://www.lagou.com/zhaopin/PHP/" data-lg-tj-id="4A00" data-lg-tj-no="0002" data-lg-tj-cid="idnull">PHP</a>                   
            <a href="https://www.lagou.com/zhaopin/C++/" data-lg-tj-id="4A00" data-lg-tj-no="0003" data-lg-tj-cid="idnull">C++</a>                     
            <a href="https://www.lagou.com/zhaopin/qukuailian/" data-lg-tj-id="4A00" data-lg-tj-no="0004" data-lg-tj-cid="idnull">区块链</a>                     
            <a href="https://www.lagou.com/zhaopin/Android/" data-lg-tj-id="4A00" data-lg-tj-no="0005" data-lg-tj-cid="idnull">Android</a>                          
            <a href="https://www.lagou.com/zhaopin/iOS/" data-lg-tj-id="4A00" data-lg-tj-no="0006" data-lg-tj-cid="idnull">iOS</a>                          
            <a href="https://www.lagou.com/zhaopin/shujuwajue/" data-lg-tj-id="4A00" data-lg-tj-no="0007" data-lg-tj-cid="idnull">数据挖掘</a>  
            <a href="https://www.lagou.com/zhaopin/shenduxuexi/" data-lg-tj-id="4A00" data-lg-tj-no="0008" data-lg-tj-cid="idnull">深度学习</a>   
            <a href="https://www.lagou.com/zhaopin/ziranyuyanchuli/" data-lg-tj-id="4A00" data-lg-tj-no="0009" data-lg-tj-cid="idnull">自然语言处理</a> 
            <a href="https://www.lagou.com/zhaopin/jiqixuexi/" data-lg-tj-id="4A00" data-lg-tj-no="0010" data-lg-tj-cid="idnull">机器学习</a>  
            <a href="https://www.lagou.com/zhaopin/ceshi/" data-lg-tj-id="4A00" data-lg-tj-no="0011" data-lg-tj-cid="idnull">测试</a>    
            <a href="https://www.lagou.com/zhaopin/html51/" data-lg-tj-id="4A00" data-lg-tj-no="0012" data-lg-tj-cid="idnull">html5</a>    
            <a href="https://www.lagou.com/zhaopin/jishuzongjian/" data-lg-tj-id="4A00" data-lg-tj-no="0013" data-lg-tj-cid="idnull">技术总监</a> 
            <a href="https://www.lagou.com/zhaopin/jiagoushi/" data-lg-tj-id="4A00" data-lg-tj-no="0014" data-lg-tj-cid="idnull">架构师</a>    
            <a href="https://www.lagou.com/zhaopin/CTO/" data-lg-tj-id="4A00" data-lg-tj-no="0015" data-lg-tj-cid="idnull">CTO</a>  '''

print("-----------匹配所有的中文------------------------")
pattern1 = re.compile(r'[\u4e00-\u9fa5]') #unicode
print(re.findall(pattern1,string))

print("-----------匹配其中的职位------------------------")
pattern2 = re.compile(r'>.*?<')
position = re.findall(pattern2,string)
for p in position:
    print(re.sub(r'>|<',"",p))             #用替换函数sub去除多余的字符

print("-----------匹配其中的链接------------------------")
pattern3 = re.compile(r'http.*?"')         # 在这里，也可以用 r'[a-zA-z]+://[^\s]*'
urls = re.findall(pattern3,string)
for url in urls:
    print(url)
