with open('seek.text','wb+') as f:
    print(f.tell())
    f.write(b'hello world!')
    print(f.tell())
    f.seek(-10,2)
    print(f.read())
    f.seek(-5,1)
    print(f.read())
    f.seek(3,0)
    print(f.read())
    print(f.fileno())


