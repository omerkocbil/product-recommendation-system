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

#plot products distribution
product_views = data['product_id'].value_counts()
sns.histplot(product_views, binwidth=1)

print(sorted(product_views))
print(f"min: {min(product_views)}, max: {max(product_views)}, \
      mode: {stat.mode(product_views)}, mean: {stat.mean(product_views)}")

#remove client's same viewing
product_data = data.groupby('product_id')['client'].apply(set) \
                   .reset_index(name='clients')
product_diff_views = [len(list) for list in product_data['clients'].to_list()]
sns.histplot(product_diff_views, binwidth=1)

print(f"min: {min(product_diff_views)}, max: {max(product_diff_views)}, \
      mode: {stat.mode(product_diff_views)}, mean: {stat.mean(product_diff_views)}")

#more than 25 viewed products
product_diff_views_gt25 = [view for view in product_diff_views if view > 25]
sns.histplot(product_diff_views_gt25, binwidth=25)

#plot views by date interval
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

data['date_intervals'] = ['morning' if 7<=time.hour<12 else 'afternoon' 
                          if 12<=time.hour<17 else 'evening' if 17<=time.hour<20 
                          else 'night' if time.hour>=20 or time.hour==0 else 'midnight' 
                          if 1<=time.hour<7 else 'error' for time in data['timestamp']]

sns.countplot(x='date_intervals', data=data)

#plot views by weekday
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data['weekday'] = [days[time.weekday()] for time in data['timestamp']]

sns.countplot(x='weekday', data=data)