import rqdatac as rq
from main import name_symbol, generate_path
import pandas as pd
import os
import numpy as np
import time


if __name__ == '__main__':
    """
    每天更新所有目标品种, 所有合约的价格
    数据颗粒度: 1min bar
    """
    rq.init()
    
    #
    date_start = '2015-01-01'
    # date_start = '2022-06-10'
    date_end = '2022-06-17' 
    
    # for symbol_cn in name_symbol:
    #     print(symbol_cn)
        
    dt_list = rq.get_trading_dates(date_start, date_end, market='cn')
    
    # name_symbol = ['RB']
                    
    for dt_temp in dt_list:
        time_start = time.time()
        print(dt_temp, end=', ')
        
        dir_year = 'D://database//database_futures//database_by_time//%d'%(dt_temp.year)
        dir_month = 'D://database//database_futures//database_by_time//%d//%d'%(dt_temp.year, dt_temp.month)
        dir_day = 'D://database//database_futures//database_by_time//%d//%d//%d'%(dt_temp.year, dt_temp.month, dt_temp.day)
        
        for symbol_cn in name_symbol:
            dir_path = 'D://database//database_futures//database_by_time//%d//%d//%d//%s'%(dt_temp.year, dt_temp.month, dt_temp.day, symbol_cn)
            contracts_list = rq.futures.get_contracts(symbol_cn, dt_temp)        
            
            for contract_temp in contracts_list:
                order_book_id = contract_temp
                df_data = rq.get_price(order_book_id, start_date=dt_temp, end_date=dt_temp, frequency='1m', fields=None, adjust_type='none', skip_suspended =False, market='cn', expect_df=True)
                
                if df_data is None:
                    pass
                else: # 存在数据
                    generate_path(dir_year)
                    generate_path(dir_month)
                    generate_path(dir_day)
                    generate_path(dir_path)
                    
                    df_data.reset_index(inplace=True)
                    col_seq = ['datetime', 'order_book_id', 'trading_date', 'open', 'high', 'low', 'close', 'volume', 'open_interest', 'total_turnover']
                    df_data = df_data[col_seq] # 调整次序
                    
                    file_path = os.path.join(dir_path, contract_temp + '.ftr')
                    df_data.to_feather(file_path)
                    
        time_end = time.time()
        print('Time: %.2f seconds'%(time_end - time_start))
                    
            

    
    