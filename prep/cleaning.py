import pandas as pd

#get data
data = pd.read_csv("../data/case_study_data_v1.csv", 
                   usecols=['client', 'timestamp', 'product_id'])

data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

#first operation - remove client's duplicate product viewing
data_v1 = data.drop_duplicates(subset = ['client', 'product_id'],
                               keep = 'first').reset_index(drop = True)