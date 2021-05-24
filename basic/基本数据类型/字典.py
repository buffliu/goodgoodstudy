# 定义一个person

import json

person = {'name': 'lifen', 'age': 18, 'occupation': '软件测试'}
#取出字典的键
for key in person.keys():
    print(key)

print(type(json.dumps(person, ensure_ascii=False)))

# items() 方法以列表返回可遍历的(键, 值) 元组数组
for key, value in person.items():
    print(key,value)

#取出字典的键
for key in person.keys():
    print(key)

#
dict2={"hobby":['singing','dancing','cooking']}

person.update(dict2)

print(f'字典加上爱好后:{person}')


# 多级字典的访问
#     创建如下：信息
#      "四川":"成都":"青城山","都江堰","宽窄巷子"
#          "广元":"剑门关","川信","红星公园"
#     输出：川信



dk_dict={
    '四川':{"成都":['青城山','都江堰','宽窄巷子'],
            "广元":['剑门关','川信','红星公园']}
}

print(dk_dict['四川']['广元'][1])


dict2={'tt':{'a':[1,2],'b':[3,4]}}


'''
通信录的例子，实现通信录，类似功能如下，练习字典的访问。
   """小王"："111"，"小李"："112",....}
   欢迎进入通信录
   1、查询联系人资料(查 指定人)
   2、插入新的联系人（存在，修改，不存在添加）
   3、删除已有联系人（删除）
   4、退出通信录
   '''

def phonebook_func1(name,phoneno):
    '''

    :param name:
    :param phoneno:
    :return:
    '''
    phonebook={'小王':'17716134341','小李':'17716134342','小张':'17716134343'}

    print(phonebook['小王'])
    phonebook[name] = phoneno

    print(f'当前通讯录显示：{phonebook}')



if __name__ == '__main__':

    phonebook_func1('小张', '23232')



