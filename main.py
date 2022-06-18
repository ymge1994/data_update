import pandas as pd
import os


contract_info = pd.read_csv('..//..//contract_info.csv', encoding='gbk')
name_symbol = contract_info['缩写'].dropna()
name_cn = contract_info['品种'].dropna()


def generate_path(path):
    """
    如果 path 不存在，则生成这个 path
    """
    if not os.path.exists(path):
        os.mkdir(path)
        
    return 0


if __name__ == '__main__':
    """
    123
    """
    pass