from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from  scipy import stats

data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")
l1= data.Total.values
l2= data.Year.values


total_Road_accidents = []
years = []
for i in range(0, 34, 3):
    y = l1[i]
    total_Road_accidents.append(y)
    z = l2[i]
    years.append(z)


total_RailRoad_accidents = []

for i in range(1, 35, 3):
    y = l1[i]
    total_RailRoad_accidents.append(y)


total_other_railway_accidents = []
for i in range(2, 36, 3):
    y = l1[i]
    total_other_railway_accidents.append(y)
print(total_RailRoad_accidents)


print(total_Road_accidents)
print(years)

y1 = total_Road_accidents
y2 = total_RailRoad_accidents
y3 = total_other_railway_accidents

x1 = years



plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Andhra Pradesh -Accidents(2001-2014)')
plt.ylabel('Road Accidents')

plt.subplot(3, 1, 2)
plt.plot(x1, y2, '.-')
plt.ylabel('RailRoad Accidents')

plt.subplot(3, 1, 3)
plt.plot(x1, y2, '.-')
plt.xlabel('Years')
plt.ylabel('Other Railway Accidents')
plt.savefig('Andhra Pradesh -Accidents(2001-2014)')

plt.show()

"""
Y=np.array(total_Road_accidents)
X=np.array(years)
Y = Y.reshape(len(Y), 1)
X=X.reshape(len(X), 1)
model = LinearRegression()
model.fit(X,Y)
Y1 = model.predict(X)

score = r2_score(X, Y1)
print(score)
"""