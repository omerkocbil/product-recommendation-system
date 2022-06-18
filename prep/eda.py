import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import seaborn as sns

#get data
data = pd.read_csv("../data/case_study_data_v1.csv", 
                   usecols=['client', 'timestamp', 'product_id'])

#get features and their data types
data.info(null_counts=True)

#get summary descriptive statistics of columns
data.describe(include='all')

#get number of duplicates entries
data.duplicated(subset=['client', 'product_id']).sum()

#plot client's product distribution
client_views = data['client'].value_counts()
sns.histplot(client_views)

print(sorted(client_views))
print(f"min: {min(client_views)}, max: {max(client_views)}, \
      mode: {stat.mode(client_views)}, mean: {stat.mean(client_views)}")

#remove same products user viewed
client_data = data.groupby('client')['product_id'].apply(set) \
                  .reset_index(name='products')
client_diff_views = [len(list) for list in client_data['products'].to_list()]
sns.histplot(client_diff_views)

print(f"min: {min(client_diff_views)}, max: {max(client_diff_views)}, \
      mode: {stat.mode(client_diff_views)}, mean: {stat.mean(client_diff_views)}")