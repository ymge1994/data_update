import pandas as pd



if __name__ == '__main__':
    """
    读取 feather 文件
    """
    file_path = 'D://database//database_futures//test//2022//6//17//RB//RB2209.ftr'
    df_read = pd.read_feather(file_path)