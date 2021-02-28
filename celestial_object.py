# ------------------------- File Header -------------------------
# Author:           Daniel Ellis
# Last Updated:     2/21/2021
# Description:
# ----------------------------- End -----------------------------

import numpy as np

class celestial_object:
    '''
    This class fully defines the orbital characteristics of celestial objects in orbit around a 'stationary' Sol.
    '''
    def __init__(self, sMajAxis, ecc, inc, lonAscNode, lonPer, meanLon, daysOrbit, radius):
        # ----- Constant Values -----
        self.a = sMajAxis                                   # Semi-Major Axis,                      AU
        self.e = ecc                                        # Eccentricity
        self.b = sMajAxis * (1.0 - ecc ** 2.0) ** (0.5)     # Semi-Minor Axis,                      AU
        self.f = sMajAxis * ecc                             # Distance from center of orbit to Sol, AU
        self.P = sMajAxis ** (3.0 / 2.0)                    # Period,                               UNITS
        self.i = inc                                        # Inclination,                          Radians
        self.OMEGA = lonAscNode                             # Longitudinal Ascending Node,          Radians
        self.PI = lonPer                                    # Longitudinal Perihelion,              Radians
        self.omega = lonPer - lonAscNode                    # Argument of Perihelion,               Radians
        self.L0 = meanLon                                   # Mean Longitude,                       Radians
        self.radius = radius * 0.00001  #6.68459e-9

        # ----- Calculated Constants -----
        self.T = -self.P * (meanLon - lonPer) \
                 / (2.0 * np.pi)                            # Time,                                 UNITS
        # this assumes T0 = 0 for midnight Greenwich mean time between Dec 31 1999, Jan 1 2000

        self.M0 = 2.0 * np.pi * (-self.T / self.P)          # Mean Anomaly at T0, UNITS
        self.yrOrbit = daysOrbit / 365.242

        self.xecliptic = []
        self.yecliptic = []
        self.zecliptic = []

        print("\nCelestial Object created")

    def orbit_creation(self, t0, tf, steps):

        time = np.linspace(t0, tf, steps)
        M = 2.0 * np.pi * (time - self.T) / self.P
        E = np.zeros(len(M))
        x = np.zeros(len(M))
        y = np.zeros(len(M))
        self.xecliptic = np.zeros(len(M))
        self.yecliptic = np.zeros(len(M))
        self.zecliptic = np.zeros(len(M))

        alph = np.array([[np.cos(self.OMEGA), np.sin(self.OMEGA), 0]])
        alphNorm = np.divide(alph, np.linalg.norm(alph))
        z = np.array([[0.0, 0.0, 1.0]])
        z0 = np.multiply(np.dot(z, np.transpose(alphNorm)), alphNorm)
        zperp = np.subtract(z, z0)
        zstar = np.cross(alphNorm, zperp)
        wscript = np.add(np.add(z0, np.cos(self.i) * zperp), np.sin(self.i) * zstar)

        wnorm = wscript
        alf = alphNorm
        alf0 = np.multiply(np.dot(alf, np.transpose(wnorm)), wnorm)
        alfperp = np.subtract(alf, alf0)
        alfstar = np.cross(wnorm, alfperp)
        uscript = np.add(np.add(alf0, np.cos(self.omega) * alfperp), np.sin(self.omega) * alfstar)
        vscript = np.cross(wscript, uscript)

        E1 = np.zeros(len(M))
        E2 = np.zeros(len(M))

        for k in range(len(M)):

            E1[k] = M[k]
            E2[k] = E1[k] - ((E1[k] - self.e * np.sin(E1[k]) - M[k]) / (1.0 - self.e * np.cos(E1[k])))
            perc = (abs((E2[k] - E1[k]) / E2[k]) * 100.0)
            while perc > 0.001:

                E1[k] = E2[k]
                E2[k] = E1[k] - ((E1[k] - self.e * np.sin(E1[k]) - M[k]) / (1.0 - self.e * np.cos(E1[k])))
                perc = (abs((E2[k] - E1[k]) / E2[k]) * 100.0)

            E[k] = E2[k]
            x[k] = self.a * np.cos(E[k]) - self.f
            y[k] = self.b * np.sin(E[k])

        for k in range(len(M)):
            ecl = x[k] * uscript + y[k] * vscript
            self.xecliptic[k] = ecl.item(0)
            self.yecliptic[k] = ecl.item(1)
            self.zecliptic[k] = ecl.item(2)

