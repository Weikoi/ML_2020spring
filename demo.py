import time
_input = '2001-10-1'
# 详见Python日期和字符串格式互相转换 //www.jb51.net/article/66019.htm
t = time.strptime(_input, '%Y-%m-%d')
print(time.strftime('%j',t))