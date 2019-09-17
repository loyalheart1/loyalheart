# with open('operation','a') as f:
#     f.write('你好')
# try:
# with open('operation','r+') as f:
#     # data=f.read(20)
#     # print(data)
#     # data=f.writelines(['\n不是\n我想要的世界'])
#     # while True:
#         # data01=f.readlines(20)
#         # if not data01:
#         #     break
#         # print(data01)
#     for line in f:
#         print(line)

# except Exception as e:
#     print(e)

#从终端输入一个单词,打印该单词和其解释,如果没有打印没有该单词

while True:
    word = input('请输入单词:')
    with open('text') as f:
        for line in f:
            data=line.split(' ')[0]
            if data>word:
                print('没有该单词')
                break
            elif data == word:
                print(line)
                break
        else:
            print('没有该单词')

    # for line in f:
    #     print(line.split(' '))#以spilt空格拆分返回的是列表

"""
从终端输入一个单词,从单词本中刚找到该单词,打印这一行内容,如果没有找到则打印"找不到"
"""
# word = input("单词:")

# 打开文件
# f = open('text')

# for line in f:
#     w = line.split(' ')[0]
# # 遍历的单词已经大于目标,说明找不到了
#     if w > word:
#        print("没有找到该单词")
#        break
#     elif w == word:
#        print(line)
#        break
# else:
#     print("没有找到该单词")
#
# f.close()