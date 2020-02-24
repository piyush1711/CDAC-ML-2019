import pandas as pd
import numpy as np

job = pd.read_csv("G:/Statistics (Python)/Datasets/JobSalary.csv")

mu_comp = job['Computer'].mean()
job['a_comp'] = job['Computer'].fillna(mu_comp)
job

job['a_comp_ff'] = job['Computer'].ffill()
job

boston = pd.read_csv("G:/Statistics (Python)/Datasets/Boston.csv")

# Column-wise mean
boston.apply(np.mean, axis=0)

# Row-wise mean
boston.apply(np.mean, axis=1)

quality = pd.read_csv("G:/Statistics (Python)/Datasets/quality.csv")
qual_melt = pd.melt(quality, id_vars='Sno')

qual_pivot = pd.pivot_table(qual_melt, index='Sno',
                            columns='variable',values='value')

qual_melt.groupby('variable')['value'].mean()

qual_melt.groupby('variable')['value'].std()

telecom = pd.read_csv("G:/Statistics (Python)/Cases/Telecom/Telecom.csv")

telecom['Response']
telecom['Response'].value_counts()

pd.crosstab(index=telecom['Response'],columns='Count')

pd.crosstab(index=telecom['Response'],columns=telecom['Gender'])

pd.crosstab(index=telecom['Response'],columns=telecom['Gender'],margins=True)

diamonds = pd.read_csv("G:/Statistics (Python)/Datasets/diamonds.csv")

pd.crosstab(index=diamonds['cut'],columns='count')
pd.crosstab(index=diamonds['color'],columns='count')

pd.crosstab(index=diamonds['cut'],columns=diamonds['color'])
pd.crosstab(index=diamonds['cut'],columns=diamonds['color'],margins=True)
