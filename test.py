import pandas as pd
import datetime
import os

files_c = os.listdir('Customers/')

for file in files_c:
    if(file.endswith('.csv')):
        df2 = pd.read_csv('Customers/' + file)
        df2['new_yearMonth'] = pd.to_datetime(df2['YearMonth'].astype(str), format='%Y%m')
        
        df2['difference'] = df2['new_yearMonth'].diff()
        df3 = df2.drop(df2['difference'].idxmax())
        df3 = df3.drop(df3['difference'].idxmin())
        
        average = df3['difference'].mean()
        date = datetime.datetime(2019, 12, 31)
        gap = date - df2['new_yearMonth'].max()
        
        if gap > average:
            df2['churn'] = '1'
            df2.to_csv('Customers_new/Customer' + file +'.csv', index=False)
        else:
            df2['churn'] = '0'
            df2.to_csv('Customers_new/Customer' + file +'.csv', index=False)
