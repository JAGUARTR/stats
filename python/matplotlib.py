# Matplotlib
import matplotlib.pyplot as plt

x =[0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 8, 27, 64, 125]

plt.plot(x, y1, label='y = x^2', color='blue', linestyle='--')
plt.plot(x, y2, label='y = x^3', color='red', linestyle='-')

plt.xlabel('X-axis')
plt.ylabel('Yaxis')
plt.title('Multiple Lines Plot')
plt.legend()

plt.show()


#B Bar Chart
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(categories, values, color='green')

plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Simple Bar Chart')

plt.show()


# C Scatter Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 7, 8, 5, 4, 6, 3, 2, 1]

plt.scatter(x, y, color='black', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()
