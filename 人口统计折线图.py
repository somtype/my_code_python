import csv
import numpy as np
from matplotlib import pyplot as plt
datax = []
datay = []
with open('WorldPopulation.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = eval(row['year'])
        if (year >= 1950):
            population = eval(
                row['World Population (Spline Interpolation until 1950)'])
            datax.append(year)
            datay.append(population)
plt.figure()
plt.plot(datax,
         datay,
         linestyle='--',
         color='#00FF00',
         markersize='3',
         markerfacecolor='#00FFFF'
         )
plt.xlabel("Year")
plt.ylabel("Population")
plt.xlim(1945, 2020)
plt.ylim(2000000000, 8000000000)
x_major_locator = plt.MultipleLocator(10)
y_major_locator = plt.MultipleLocator(1000000000)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.show()
