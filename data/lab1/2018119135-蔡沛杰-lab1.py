import pandas as pd

excel_file = r'/home/cpj/python/lab1/SH#600519.xlsx'

sheet = pd.read_excel(excel_file, sheet_name='SH#600519')

df = pd.DataFrame(sheet)

'''
修改列标题
'''
head = df.columns.values.tolist()

for i in range (len(head)):
    df.rename(columns={head[i]:df.iloc[0,i]},inplace=True)


'''
删除第一行
'''
df = df.drop(0,axis=0,inplace=False)


#==============i======================
date = input("\n请输入日期:\n")
print('\n')
date_ = pd.to_datetime(date)
test1 = df[df['日期']==date_]
print(test1)

#=============ii======================
peak_of_day = (int)(input("\n请输入最大最高值:\n"))
print('\n')
print(df[
            df['最高'] > peak_of_day
        ])
'''
for i in range(len(df)):
    if(df.iloc[i,2] > peak_of_day):
        print(df.iloc[i,0])    
'''
#============iii======================
wave = (float)(input("\n请输入最小波动:\n"))

print('\n')
print( df[ 
            df['最高']> ( wave+df['最低'] ) 
         ])
'''
for i in range(len(df)):
    if(df.iloc[i,2] > (wave+df.iloc[i,3]) ):
        print(df.iloc[i,0])
'''
#============iv=======================

flag_2 = (int)(input("\n请输入最小成交量:\n"))
print('\n')
print(df[
       df['成交量'] > flag_2
     ])

'''
for i in range(len(df)):
    if(df.iloc[i,5] > flag_2):
        print(df.iloc[i,0])
'''
#============v========================

sums = (int)(input("\n请输入最小成交额: \n"))
print('\n')
print(df[
        df['最高'] > peak_of_day
     ])
'''
for i in range(len(df)):
    if(df.iloc[i,6] > sums):
        print(df.iloc[i,0])
'''
