import pandas as pd
import matplotlib.pyplot as plt

IMAGE_NAME = 'iris_data_chart.png'

dataset = pd.read_csv('iris_data.csv')
setosa=dataset[dataset['Species']=='setosa']
versicolor =dataset[dataset['Species']=='versicolor']
virginica =dataset[dataset['Species']=='virginica']



#for each Species ,let's check what is petal and sepal distibutuon
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

setosa.plot(x="Sepal_Length", y="Sepal_Width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="Sepal_Length",y="Sepal_Width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="Sepal_Length", y="Sepal_Width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="Petal_Length", y="Petal_Width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="Petal_Length",y="Petal_Width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="Petal_Length", y="Petal_Width", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

fig.savefig(IMAGE_NAME)