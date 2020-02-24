import pandas as pd
import os
os.chdir("G:/Statistics (Python)/Datasets")
mum = pd.read_csv("mum_members.csv")
delhi = pd.read_csv("Delhi_members.csv")

print(mum)
print(delhi)

comb1 = mum.append(delhi)
comb1

comb1.loc[1]

comb1 = mum.append(delhi).reset_index()
comb1

comb1 = mum.append(delhi).reset_index(drop=True)
comb1

## Using concat

comb2 = pd.concat([mum, delhi])
comb2

comb2 = pd.concat([mum, delhi],ignore_index=True)
comb2

###########################################

aster = pd.read_csv("Aster.csv",index_col=0)
rose = pd.read_csv("Rose.csv",index_col=0)

flower_sales = pd.concat([aster,rose],axis='columns')
flower_sales = pd.concat([aster,rose],keys = ['aster','rose'],axis='columns')
###################################
## Merging
demog = pd.read_csv("demo_age.csv")
rating = pd.read_csv("Ratings.csv")

dem_rat = demog.merge(rating,on="Name")
#OR
dem_rat = demog.merge(rating,left_on="Name",right_on="Name")

dem_rat = demog.merge(rating,how='left',on="Name")
dem_rat = demog.merge(rating,how='right',on="Name")
dem_rat = demog.merge(rating,how='outer',on="Name")
