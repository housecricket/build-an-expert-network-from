from matplotlib import pyplot as plt
from data import *

# create a line chart, years on x-axis, incomes on y-axis
years = []
incomes = []
labels = []
for i in range(0, 9):
    years.append(incomes_and_tenures[i][1])
    incomes.append(incomes_and_tenures[i][0])
    labels.append(experts[i]["name"])

plt.scatter(years, incomes, color='green')

# label each point
for label, years_count, incomes_count in zip(labels, years, incomes):
    plt.annotate(label,
        xy=(years_count, incomes_count), # Put the label with its point
        xytext=(5, -5),                  # but slightly offset
        textcoords='offset points')

plt.title("Income by Years Experience")
plt.xlabel("Year")
plt.ylabel("Income")
plt.show()


