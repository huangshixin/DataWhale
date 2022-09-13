import numpy as np

import pandas as pd

#【查看版本】
# print(pd.__version__)


#Creating a Series by passing a list of values, letting pandas create a default integer index:
#【一维数组】创建一个Series，通过使用一个list，让pandas创建一个默认的整型角标---生成序列的列
s = pd.Series([1, 3, 5, np.nan, 6, 8]) #也可以使用字典形式存入  此外 s[:3] 也可以实现
'''
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
'''


#【如何指定数组元素的---数据类型呢？】
#【二维数组】
#pd.DataFrame --- pd.DataFrame(ndarray数据，index=[‘行索引1’，‘行索引2’]，colunms=[‘列索引1’，‘列索引2’])
dates = pd.date_range("20130101", periods=6)
data1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) #后序两个数 index 和 colunms都是需要接收list的
'''
                   A         B         C         D
2013-01-01 -0.161697 -1.457249  1.706196  1.018571
2013-01-02  1.016481  2.247334 -1.393633 -0.119382
2013-01-03 -0.384872  1.495994 -0.681358  1.289184
2013-01-04  1.309894 -0.482228  0.788780 -1.282365
2013-01-05 -0.245477 -1.418557  0.818713 -0.972759
2013-01-06  1.076599  0.685614 -1.222039 -1.517841
'''


df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)
'''
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo

【注意】pandas在字段列不匹配的时候，会选择’半自动‘填充；这种情况不适合数据分析
'''


#【查看pandas中的数据类型】

'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object

'''



#【查看二维列表中的数据】---可以指定看多少行，只需要往其中输入数据即可
view1 = data1.head()#查看前5行
view2 = data1.tail()#查看后5行
# print(data1.head(10))


#【取行和列】
# print(data1.index)
# print(data1.columns)
'''
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
Index(['A', 'B', 'C', 'D'], dtype='object')
'''


#【类型转换---转numpy】
#does not include the index or column labels in the output.---不包含---行和列
# print(data1.to_numpy())
'''
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
'''
print(df2.to_numpy())
'''
[[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]

'''
