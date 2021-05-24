import xlrd

#创建工作簿对象

def excelread(sheetname2,inputdata,expectdata):
    work_book=xlrd.open_workbook_xls('../data/外卖系统接口测试用例-V1.5.xls')

    #查看excle中有多少个sheety 页

    sheetnames=work_book.sheet_names()

    for sheetname in sheetnames:
        print(sheetname)

    logintable=work_book.sheet_by_name(sheetname2)

    #一共有多少列
    print(logintable.ncols)
    #一共有多少行
    print(logintable.nrows)

    # for row in range(0,logintable.nrows):
    #
    #     print(logintable.row_values(row,0,logintable.ncols))


    #读取指定列值
    datalist=[]
    for row in range(1, logintable.nrows):
        datalist.append((logintable.cell(row,inputdata),logintable.cell(row,expectdata)))

    return datalist

if __name__ == '__main__':

    excelread('登录模块',9,11)