import re
string = 'hello xdbcb8'
pattern = 'hello'
flag = re.match(pattern, string) # match the pattern to the string
if flag: # return None if not match, and return an sre object
	print('match')
else:
	print('not match')

#############################################
import re
string = 'hello xdbcb8'
pattern = 'xdbcb'
flag = re.search(pattern, string)
print(flag)
if flag: # return None if not match, and return an sre object
	print('search')
else:
	print('no result')

############################################
import re
link = '<a href="(.*)">(.*)</a>'
url = '<a href="http://www.baidu.com">baidu</a>'
info = re.findall(link, url) # 获取非重复的匹配列表
print(info)
#############################################
import re
m = re.split('(\d+)', 'dkjj23jjj44')
print(m)
#############################################
import re
a = "789xyz123"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))
############################################
import re
a = "789xyz123"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).groups())


'''
密码构建：

强：字母+数字+特殊字符，长度大于10位

中：字母+数字，字母+特殊字符，数字+特殊字符，长度在6-10之间

弱：纯数字，纯字母，纯特殊字符（含大小写），长度小于6位
'''