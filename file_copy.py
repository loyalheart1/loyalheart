oldflie=input('请输入要复制的文件:')
newflie=input('请输入要复制到哪里:')
with open(oldflie,'rb') as f:
    while True:
        data=f.read(1024)
        if not data:
            break
        with open(newflie,'wb+') as e:
            e.write(data)