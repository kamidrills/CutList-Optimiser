import matplotlib.pyplot as plt
import random
import matplotlib.cm as cm
import numpy as np


def fit_orders_on_sheet(sheet_width, sheet_height, orders):
    x = 0
    y = 0
    current_height = 0
    fig, ax = plt.subplots()
    color = iter(cm.rainbow(np.linspace(0, 1, len(orders))))
    for order in orders:
        c = next(color)
        if x + order[0] > sheet_width or current_height + order[1] > sheet_height:
            x = 0
            y = 0
            current_height = 0
        rect = plt.Rectangle((x, y), order[0], order[1], fill=True, color=c)
        ax.add_patch(rect)
        ax.annotate(str(order[0]) + 'x' + str(order[1]), (x + order[0] / 2, y + order[1] / 2), color='white',
                    ha='center', va='center')
        x += order[0]
        current_height = max(current_height, order[1])
        if x + order[0] > sheet_width:
            x = 0
            y = current_height
    ax.set_xlim(0, sheet_width)
    ax.set_ylim(0, sheet_height)
    ax.set_aspect('equal', adjustable='box')
    plt.show()


sheet_width = int(input("Enter the width of the sheet: "))
sheet_height = int(input("Enter the height of the sheet: "))

orders = []
num_orders = int(input("Enter the number of orders: "))
for i in range(num_orders):
    width = int(input("Enter the width of order {}: ".format(i + 1)))
    height = int(input("Enter the height of order {}: ".format(i + 1)))
    orders.append((width, height))

fit_orders_on_sheet(sheet_width, sheet_height, orders)
