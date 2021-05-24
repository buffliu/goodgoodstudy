'''
随机生成一个列表a，10个元素。打乱顺序，然后求a的最大值，最小值，和，平均值，
      显示从大到小的顺序
'''

import random
a=[]
def list_func1(len):
    for i in range(len):
        a.append(random.randint(1,len))
    maxvalue=max(a)
    minvalue=min(a)
    sumvalue=sum(a)

    avgvalue=sumvalue/10

    sortvalue=sorted(a)

    print(f'a的最大值{maxvalue}，最小值{minvalue}，和{sumvalue}，平均值{avgvalue}，显示从大到小的顺序{sortvalue}')


'''
随机生成一个列表a，10个元素都小于10.插入元素5，在第六个位置插入元素99，输出最大值，
     输出奇数位的值。
'''
b=[]
def listfunc2():
    for i in range(0,10):
        b.append(i)
    b.append(5)
    b.insert(6,99)
    maxvalue=max(b)
    newb=[]
    for i in range(1,len(b),2):
        newb.append(b[i])

    print(f'原始b:{b},最大值：{maxvalue},奇数位：{newb}')



list=[]

list.append((1,2))

if __name__ == '__main__':
    list_func1(10)
    listfunc2()
    print(list)




