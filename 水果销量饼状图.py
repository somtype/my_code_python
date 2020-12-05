import matplotlib.pyplot as plt
saled = [200, 250, 150, 300, 100]
labels = ['Apple', 'Pear', 'Lemon', 'Mango', 'Cheery']
explode = [0.1, 0, 0.1, 0, 0]
plt.figure()
plt.pie(saled, explode=explode, labels=labels, autopct="%1.1f%%", shadow=True)
plt.show()
