
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[46]:


file_flag = input("请输入股票名：")
if file_flag == '1' or True:
    csv_file = r'/home/cpj/python/data/lab2/data/600519.csv'

    csv = pd.read_csv(csv_file, encoding='gb18030')

    df = pd.DataFrame(csv)
    date =  '2020-09-17'
    test1 = df[df['日期']==date_]
    print(test1)


# In[57]:


file_flag = input("请输入股票名：")
if file_flag == '1' or True:
    csv_file = r'/home/cpj/python/data/lab2/data/600519.csv'

    csv = pd.read_csv(csv_file, encoding='gb18030')

    df = pd.DataFrame(csv)
    date =  input("输入日期")
    test1 = df[df['日期']==date_]
    print(test1)


# In[57]:


print('请输入股票名：\n1\n输入日期\n2020-09-17\n')
print(df[df['日期']=='2020-09-17'])


# In[61]:


flag = (float)(input())
df[df['收盘价']>flag]


# In[69]:


flag = input()
df[df['涨跌幅']>flag]


# In[71]:


flag = (int)(input())
df[df['成交量']>flag]


# In[71]:


flag = (int)(input())
df[df['成交量']>flag]


# In[73]:


flag = (int)(input())
df[df['成交金额']>flag]


# In[64]:


df.iloc[1,10].dtype


# In[73]:


flag = (int)(input())
df[df['成交金额']>flag]


# In[74]:


def marge(csv_list, outputfile):
    for inputfile in csv_list:
        f = open(inputfile, 'r', encoding='gb18030',errors='ignore')
        data = pd.read_csv(f,encoding='gb18030')
        data.to_csv(outputfile, mode='a', index=False)
    print('完成合并')
 
 #去重保留一个表头
def distinct(file):
    df = pd.read_csv(file, header=None)
    datalist = df.drop_duplicates()
    datalist.to_csv( index=False, header=False)
    print('完成去重')


# In[79]:


csv_file = r'/home/cpj/python/data/lab2/data/margin.csv'
csv = pd.read_csv(csv_file)
df = pd.DataFrame(csv)


# In[78]:


df


# In[80]:


flag = input()
df[df['涨跌幅']>flag]


# In[82]:


flag = input("请输入日期：\n2019-08-08")
df[df['日期']==flag]


# In[84]:


flag = input()
df[df['成交量']>flag]


# In[87]:


flag = (input())
df[df['成交金额']>flag]

