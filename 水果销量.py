import matplotlib.pyplot as plt
saled = [200, 250, 150, 300, 100]
labels = ['Apple', 'Pear', 'Lemon', 'Mango', 'Cheery']
plt.figure()
plt.pie(saled, labels=labels, autopct="%1.1f%%")
plt.show()
