import pandas as pd

#get data without 
data = pd.read_csv("../data/case_study_data_v1.csv", usecols=['client', 'timestamp', 'product_id'])

#get features and their data types
data.info(null_counts=True)

#get summary descriptive statistics of columns
data.describe(include='all')

#get number of duplicates entries
data.duplicated(subset=['client', 'product_id']).sum()