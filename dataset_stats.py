import pandas as pd
from shutil import copyfile


df = pd.read_csv('/Users/mona/Downloads/gun_violence_student_coders.csv')

print(df.shape)
print(df.groupby(df['Q1 Relevant']).describe())

#print(df_all.groupby(df_all['Q3 Theme1']).describe())

#print(df_all.shape)

