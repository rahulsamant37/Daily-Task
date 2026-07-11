import random
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


size = 1000            # 1000 * 1000
# fill_percent = 59.27 # threshold
# uncertain zone width -> size ^ (-3/4)
# fill_percent = 59.84 # 59.27 + 1000 ^ (-3/4) = 59.27 + 0.57 
fill_percent = 58.60 # 59.27 - 1000 ^ (-3/4) = 59.27 - 0.57 
animation_delay = 20

total_cells = size * size
num_people = round(total_cells * fill_percent / 100)

grid = np.zeros((size, size), dtype=np.uint8)
positions = np.random.choice(total_cells, size = num_people, replace = False)
grid.flat[positions] = 1

start = np.random.choice(positions)
start_row, start_col = divmod(start, size)
grid[start_row, start_col] = 2

frontier = [(start_row, start_col)]

frames = [grid.copy()]

while frontier:
    new_frontier = []

    for row, col in frontier:
        neighbors = [
            (row, col+1),
            (row, col-1),
            (row+1, col),
            (row-1, col),
        ]
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < size and 0 <= neighbor_col < size:
                if grid[neighbor_row, neighbor_col] == 1:
                    grid[neighbor_row, neighbor_col] = 2
                    new_frontier.append((neighbor_row, neighbor_col))
    frontier = new_frontier

    if frontier:
        frames.append(grid.copy())

fig, ax = plt.subplots(figsize=(7, 7))

img = ax.imshow(frames[0], interpolation = 'nearest', vmin=0, vmax=2)
ax.axis('off')
title = ax.set_title(f'Fill: {fill_percent}% | People: {num_people} | Infected: 1')

def update(frame_index):
    frame = frames[frame_index]
    img.set_data(frame)

    infected_count = np.sum(frame == 2)

    title.set_text(f'Fill: {fill_percent}% | People: {num_people} | Infected: {infected_count}')
    return img, title

animation = FuncAnimation(
        fig,
        update,
        frames = len(frames),
        interval = animation_delay,
        blit = False,
        repeat = False
        )
plt.show()

