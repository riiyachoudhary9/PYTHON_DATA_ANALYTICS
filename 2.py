import matplotlib.pyplot as plt

names = ['Aman', 'Riya', 'Karan', 'Neha']
marks = [78, 92, 65, 88]

# Bar Chart
plt.bar(names, marks)
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Bar Chart')
plt.show()

# Line Chart
plt.plot(names, marks, marker='o')
plt.title("Line Chart")
plt.show()

# Pie Chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
