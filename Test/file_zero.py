"""
空洞文件
"""
with open('test','wb+') as f:
    f.write('你好阿,世界！'.encode())
    f.seek(1024*1024*10,1)
    f.write(b'hello world')
    data=f.read(10)
    print(data)

