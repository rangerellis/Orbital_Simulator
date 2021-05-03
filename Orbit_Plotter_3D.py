# ------------------------- File Header -------------------------
# Author:           Daniel Ellis
# Last Updated:     2/21/2021
# Description:
# ----------------------------- End -----------------------------

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Orbit_Plotter_3D:
    '''
        This class handles the 3D animations of celestial object orbits.
    '''
    def __init__(self):

        # Indicates Initialization
        self.flagInit = True

        # Initializes figure and axes object
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Instantiate lists to hold data histories
        self.time_history = []  # Time
        self.x_history = []     # x-coordinate
        self.y_history = []     # y-coordinate
        self.z_history = []     # z-coordinate

        x = self.ax.plot3D([0, 1], [0, 0], [0, 0], 'red')
        y = self.ax.plot3D([0, 0], [0, 1], [0, 0], 'green')
        z = self.ax.plot3D([0, 0], [0, 0], [0, 1], 'blue')
        self.bounds = 5
        self.ax.axes.set_xlim3d(left=-self.bounds, right=self.bounds)
        self.ax.axes.set_ylim3d(bottom=-self.bounds, top=self.bounds)
        self.ax.axes.set_zlim3d(bottom=-self.bounds, top=self.bounds)

        # Create a handle for each object
        self.handle = []

        self.diameterSun = 20 * 0.00929826069  # in AU
        self.u = np.linspace(0, 2 * np.pi, 50)
        self.v = np.linspace(0, np.pi, 50)

        self.x_sun = np.outer(np.cos(self.u), np.sin(self.v))
        self.y_sun = np.outer(np.sin(self.u), np.sin(self.v))
        self.z_sun = np.outer(np.ones(np.size(self.u)), np.cos(self.v))

        self.ax.plot_surface(self.diameterSun * self.x_sun, self.diameterSun * self.y_sun, self.diameterSun * self.z_sun, color="yellow")

        plt.draw()

        print("\n3D Plot successfully initialized")

    def update_plot(self, x, y, z, orbitNo, radius):

        self.ax.cla()
        self.ax.plot_surface(self.diameterSun * self.x_sun, self.diameterSun * self.y_sun,
                             self.diameterSun * self.z_sun, color="yellow")
        self.ax.plot3D([0, 1], [0, 0], [0, 0], 'red')
        self.ax.plot3D([0, 0], [0, 1], [0, 0], 'green')
        self.ax.plot3D([0, 0], [0, 0], [0, 1], 'blue')
        self.ax.axes.set_xlim3d(left=-self.bounds, right=self.bounds)
        self.ax.axes.set_ylim3d(bottom=-self.bounds, top=self.bounds)
        self.ax.axes.set_zlim3d(bottom=-self.bounds, top=self.bounds)

        if len(self.handle) < orbitNo:
            self.flagInit = True
            print("Flag initialized: ", orbitNo)

        self.plot_orbit(x, y, z, orbitNo, radius)

    def plot_orbit(self, x, y, z, orbitNo, radius):

        x_object = x[-1] + self.diameterSun * np.outer(np.cos(self.u), np.sin(self.v))
        y_object = y[-1] + self.diameterSun * np.outer(np.sin(self.u), np.sin(self.v))
        z_object = z[-1] + self.diameterSun * np.outer(np.ones(np.size(self.u)), np.cos(self.v))

        if self.flagInit == True:

            # Create the celestial object patch and append it to the handle list
            self.handle.append(
                [x, y, z, orbitNo, self.diameterSun, x_object, y_object, z_object])

            for k in range(0, len(self.handle), 1):
                self.ax.plot3D(self.handle[k][0], self.handle[k][1], self.handle[k][2])
                self.ax.plot_surface(self.handle[k][5], self.handle[k][6],
                                     self.handle[k][7], color="yellow")

            self.flagInit = False
        else:

            for k in range(0, len(self.handle), 1):

                if orbitNo == self.handle[k][3]:

                    self.handle[k] = [x, y, z, orbitNo, self.diameterSun, x_object, y_object, z_object]
                    self.ax.plot3D(x, y, z)
                    self.ax.plot_surface(self.handle[k][5], self.handle[k][6],
                                         self.handle[k][7], color="yellow")
                else:
                    self.ax.plot3D(self.handle[k][0], self.handle[k][1], self.handle[k][2])
                    self.ax.plot_surface(self.handle[k][5], self.handle[k][6],
                                         self.handle[k][7], color="yellow")
