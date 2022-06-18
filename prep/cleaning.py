import pandas as pd

#get data
data = pd.read_csv("../data/case_study_data_v1.csv", 
                   usecols=['client', 'timestamp', 'product_id'])

data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

#first operation - remove client's duplicate product viewing
data_op1 = data.drop_duplicates(subset = ['client', 'product_id'],
                               keep = 'first').reset_index(drop = True)

#second operation - remove clients with only 1 product view
client_data = data_op1.groupby('client')['product_id'].apply(list) \
                  .reset_index(name='products')
                  
client_data['view_count'] = [len(product_list) 
                             for product_list in client_data['products']]

customers_to_be_removed = client_data[client_data['view_count'] == 1]['client'].to_list()
data_op2 = data_op1[~data_op1['client'].isin(customers_to_be_removed)]