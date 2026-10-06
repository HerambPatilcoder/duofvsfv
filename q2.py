import pandas as pd
import os
new_path = "/Users/herambpatil/Documents/cs699/assign2/students.csv"
csv_ = pd.read_csv(new_path)

if os.path.exists(new_path):
    print(csv_.shape[0])
    df1 = csv_[csv_['Department']=='CSE']
    print(df1.shape[0])
    print(csv_[csv_['Department']=='EE'])