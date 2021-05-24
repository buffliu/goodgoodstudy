try:
    with open('1.txt', 'r')as rf:
        rf.readline()
except IOError as err:  # 输入/输出操作失败
    print(err)

else:
    print('你好')
    
