
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv("F:/Python Material/Python Course/Datasets/iris.csv")
sns.pairplot(iris, hue="Species")
plt.show()


df = pd.read_csv('G:/Statistics (Python)/Datasets/cars2018.csv')
df_ana = df[['Displacement','Transmission', 'MPG','Max Ethanol']]

sns.pairplot(df_ana, hue="Transmission")
plt.show()

#####################################################################
sns.scatterplot(x='Displacement',y='MPG',hue="Transmission",data=df)
plt.show()
###################################################################

sns.scatterplot(x='Displacement',y='MPG',
                hue="Transmission",size='Max Ethanol',data=df)
plt.show()