import pandas as pd

excel_file = r'/home/excel/python_program/data/SH#600519.xlsx'

data = pd.read_excel(excel_file)

df = pd.DataFrame(data)


'''
原列名
'''
head = df.columns.values.tolist()

'''
修改列名：
    df.rename(columns={'原列名'：'新列名'},inplace=True)
'''
for i in range (len(head)):
    df.rename(columns={head[i]:df.iloc[0,i]},inplace=True)

'''
修改后的列名
'''
head=df.columns.values.tolist()

'''
删除第一行
'''
df = df.drop(0,axis=0,inplace=False)


#-------------------------------------
date = input()
dates = pd.to_datetime(date)

#-------------------------------------
flag=0
df.loc[(df[head[0]]==dates),
        [head[0],head[1],head[2],
            head[3],head[4],head[5],head[6]]
        ].head()

#-------------------------------------
wave = (float)(input())
df.loc[ ( df[head[2]] > (wave+df[head[3]]) ),
        [head[0],head[1],head[2],
         head[3],head[4],head[5],head[6]]
      ].head()


#-------------------------------------

turnover = (int)(input())
df.loc[(df[head[5]]>turnover),
       [head[0],head[1],head[2],
        head[3],head[4],head[5],head[6]]
      ].head()

#-------------------------------------

sums = (int)(input())
df.loc[(df[head[6]]>sums),
       [head[0],head[1],head[2],
        head[3],head[4],head[5],head[6]]
      ].head()

#-------------------------------------
