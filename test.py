import numpy as np
import matplotlib.pyplot as plt

# Get stock width and height from user
stock_width, stock_height = map(int, input("Enter stock width and height (space-separated): ").split())

# Get number of orders from user
num_orders = int(input("Enter number of orders: "))

# Get the width and height of each order
orders = []
for i in range(num_orders):
    order_width, order_height = map(int, input("Enter order {} width and height (space-separated): ".format(i+1)).split())
    orders.append((order_width, order_height))

# Plot the stock sheet
fig, ax = plt.subplots()
ax.set_xlim([0, stock_width])
ax.set_ylim([0, stock_height])
ax.set_aspect('equal', adjustable='box')

# Generate different colors for each order
colors = plt.cm.jet(np.linspace(0, 1, num_orders))

for i, (order_width, order_height) in enumerate(orders):
    x = i * (order_width + 10)
    y = 0
    ax.add_patch(plt.Rectangle((x, y), order_width, order_height, fill=True, color=colors[i]))
    ax.annotate("{} x {}".format(order_width, order_height), (x+order_width/2, y+order_height/2), ha='center', va='center')

plt.show()
