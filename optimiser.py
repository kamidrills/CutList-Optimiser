import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class CutListOptimizer:
    def __init__(self, stock_width, stock_height, cuts):
        self.stock_width = stock_width
        self.stock_height = stock_height
        self.cuts = cuts
        self.plan = []
        self.remaining_space = [(0, 0, stock_width, stock_height)]

    def can_fit(self, cut, space):
        cut_w, cut_h = cut
        x, y, w, h = space
        return cut_w <= w and cut_h <= h

    def update_remaining_space(self, space, cut):
        cut_w, cut_h = cut
        x, y, w, h = space

        new_spaces = []
        if h - cut_h > 0:
            new_spaces.append((x, y + cut_h, w, h - cut_h))
        if w - cut_w > 0:
            new_spaces.append((x + cut_w, y, w - cut_w, cut_h))

        return new_spaces

    def optimize(self):
        self.plan.clear()
        self.remaining_space = [(0, 0, self.stock_width, self.stock_height)]

        for cut in self.cuts:
            for i, space in enumerate(self.remaining_space):
                if self.can_fit(cut, space):
                    self.plan.append((cut, space[:2]))
                    new_spaces = self.update_remaining_space(space, cut)
                    self.remaining_space.pop(i)
                    self.remaining_space.extend(new_spaces)
                    break

    def display_plan(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.stock_width)
        ax.set_ylim(0, self.stock_height)

        for cut, pos in self.plan:
            rect = Rectangle(pos, cut[0], cut[1], edgecolor='black', facecolor='cyan', fill=True)
            ax.add_patch(rect)
            ax.text(pos[0] + cut[0] / 2, pos[1] + cut[1] / 2, f"{cut[0]}x{cut[1]} mm", ha='center', va='center')

        ax.set_title("Cutting Plan (mm)")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
