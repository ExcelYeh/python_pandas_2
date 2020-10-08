# coding: utf-8

import pandas as pd
import os
import glob
import pprint


class CsvFile:
    def __init__(self, file_path):
        self.file_path =  file_path


class Solutions:
    '''
        csv文件处理
    '''
    def __init__(self, CsvFile):
        '''
            初始化函数，
            属性： CsvFile： CsvFile对象
        '''
        self.CsvFile =  CsvFile
    
        
    def get_idx(self, flag, lists):
        '''
            @brief：返回 flag 在lists第一次出现的下标
            @param: flag: 待寻找的元素
                    lists:集合
        '''
        idx = 0
        while idx<len(temp) and temp[idx]!=char:
            idx+=1
        return idx
    
    def get_last_index(self, flag, lists):
        '''
            获取 flag 在 lists 最后一次出现的下标
            思路： 反转字符串后， 寻找第一次出现的下标
        '''
        temp = strs[::-1]  # 反转字符串
        idx = self.get_idx(self, flag, temp)
        return (len(temp)-1-idx)
    
    def get_id_name(self):
        '''
            对属性 file_path 处理，得到csv文件对应的股票代码
        '''
        begin_char = '/'
        end_char = '.'
        begin_index = get_last_index(self.CsvFile.file_path, 
                                          begin_char) + 1
        end_index = get_last_index(self.CsvFile.file_path,
                                        end_char)
        return self.CsvFile.file_path[begin_index, end_index]
    
    
    def get_df(self):
        '''
            通过属性 file_path 处理csv数据，得到 DataFrame
        '''
        file = pd.read_csv(self.CsvFile.file_path)
        df = pd.DataFrame(file)
        return df
    
    def get_df_head_list(self):
        '''
            无参构造，得到列标题
        '''
        df = self.get_df()
        head_list = df.columns.values.tolist()
        return head_list
    
    def search_equal(self, head, val, show_head_list):
        
        '''
            寻找在 head 这一列中 值为 val的行，显示内容由 show_head_list 决定
        '''
        #-----------------------------------------
        '''
        df_head_list = self.get_df_head_list()
        head = df_head_list[head_idx]
        '''
        #-----------------------------------------
        df = self.get_df()
        return df.loc[ (df[head] == val), 
                show_head_list]
    def search_cmp(self,head, val, show_head_list):
        '''
            寻找在 head 这一列中 值> val的行，显示内容由 show_head_list 决定
        '''
        df = self.get_df()
        return df.loc[ (df[head] > val), 
                       show_head_list ]


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


csv_list = glob.glob(os.getcwd()+'/data/*.csv')
output_csv_path = 'data/margin.csv'
print(csv_list)
marge(csv_list, output_csv_path)
distinct(output_csv_path)


pd.DataFrame(pd.read_csv(file_path))



def get_file_list(path):
    '''
    给出
    '''
    # ['600519.csv', '000858.csv']
    path_file_short_list = os.listdir(path) 
    path_file_full_list  = []
    for files in path_file_list:
        path_file_full = os.path.join(path, files)
        path_file_full_list.append(path_file_full)
    return path_file_full_list


def main():
    csv_list = glob.glob(os.getcwd()+'/data/*.csv')
    margin_file_path = os.getcwd()+'/data/margin.csv'
    if margin_file_path not in csv_list:
        output_csv_path = 'data/margin.csv'
        marge(csv_list, output_csv_path)
        distinct(output_csv_path)
        pwd = os.getcwd()+'/data'    # csv文件所在目录
        csv_list = glob.glob(os.getcwd()+'/data/*.csv')
    print(csv_list)
    file = CsvFile(csv_list[0]) # 读取第一个csv文件，新建CsvFile对象，
    test = Solutions(file)
    show_list = test.get_df_head_list()
    #pprint.pprint(test.get_df())
    print(test.search_cmp('成交金额', '912323410', show_list).head())


if __name__ =='__main__':
    main()


