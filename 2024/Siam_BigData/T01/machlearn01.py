import numpy as np
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression

x=[1,2,3,4,5,6,7,8,9,10]
y=[34,45,34,54,45,56,67,56,45,57]

model=LinearRegression()
X=np.array(x).reshape(-1,1)
model.fit(X,y)

features=X
x_per_previsione=np.array([[11],[12],[13],[14]])
x_totali=np.concatenate((features,x_per_previsione))

target = y
previsione = model.predict(x_totali)

mp.scatter(features, target)
mp.plot(x_totali,previsione, color="orange")
mp.scatter(x_per_previsione, previsione[-len(x_per_previsione):],
           marker='s',s=100,color="blue")
mp.show()