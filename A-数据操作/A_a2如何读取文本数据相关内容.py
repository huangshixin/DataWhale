import pandas as pd
import numpy as np

#【两种读取方式】
#read_csv
file1 = pd.read_csv(
    filepath_or_buffer='../Datafile/csdata.csv',
    sep=',',#列分割符号
    encoding='utf-8',#格式编码utf-8--------unicode需要指定的编码格式进行解码
    names=None,#行名字
    # index_col=,#列名字
)

file2 = pd.read_table(filepath_or_buffer='../Datafile/csdata.csv',sep=',',encoding='utf-8')#必须要sep


#读取excel的数据
'''read-excel'''
#读取excel文件的时候，直接按照文件的地址进行识别即可
file3 = pd.read_excel('../Datafile/school.xlsx',sheet_name=0)#默认python的读取方式

pd.read_clipboard()#从剪切榜获取信息
pd.read_json()
pd.read_sql()#需要读取sql文件的信息
pd.read_sql_query()#需要sql语句
pd.read_sql_table()#查询表


'''
将pandas中的DataFrame装欢为其它数据格式的命令

1、首先，你需要先声明一个DataFrame类

之后，你才可以进行转换

to_dict()
to_numpy()
to_markdown()
to_records()
to_latex()
'''



