import random
import matplotlib.pyplot as plt
import numpy as np

# width and height of canvas in pixels
size = 750
# number of random complex numbers to generate
complex_count = 5000000
# how many iterations of z^2 + c formula are to be used?
iter_count = 750

# set up the graph
fig, ax = plt.subplots()

# create an array of boxes
boxes = np.zeros(size * size).reshape(size, size)

# main loop
for j in range(complex_count):
    exceeded_2 = False

    # generate a new random complex number
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    c = x + y * 1j

    # z always starts from 0
    z = 0

    # keep track of the values of z at each step
    path = []

    # determine if c belongs to Mandelbrot set or not
    for i in range(iter_count):
        path.append([z.real, z.imag])
        z = z * z + c
        # if the magnitude of z exceeds 2, get out of the for cycle
        if abs(z) > 2:
            exceeded_2 = True
            break

    # mark the points visited during the escape in the array
    if exceeded_2:
        for point in path:
            # translate the complex plane coordinates into actual pixels
            x_pixel = int(point[0] / 2 * (size / 2) + size // 2)
            y_pixel = int(point[1] / 2 * (size / 2) + size // 2)

            # TODO: Fix this if statement, looks clumsy
            # omit the [0, 0] points
            if not point == [0, 0]:
                boxes[x_pixel][y_pixel] += 1

# zoom in
plt.axis([size * 0.15, size * 0.85, size * 0.75, 0])

# translate the array into a graph and show it
img = ax.imshow(boxes)
plt.show()
