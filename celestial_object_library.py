# ------------------------- File Header -------------------------
# Author:           Daniel Ellis
# Last Updated:     2/21/2021
# Description:
# ----------------------------- End -----------------------------

import math

class celestial_object_library:
    '''
    This class contains the information to fully define the orbital characteristics of celestial objects in orbit around
    a 'stationary' Sol.
    '''
    def __init__(self):

        self.Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        self.Pa = [0.38709893, 0.72333199, 1.00000011, 1.52366231,
                   5.20336301, 9.53707032, 19.19126393, 30.06896348]         # Semi-Major Axis, AU
        self.Pe = [0.20563069, 0.00677323, 0.01671022, 0.09341233,
                   0.04839266, 0.05415060, 0.04716771, 0.00858587]             # Eccentricity
        self.Pi = [math.radians(7.00487), math.radians(3.39471),
                   math.radians(0.00005), math.radians(1.85061),
                   math.radians(1.30530), math.radians(2.48446),
                   math.radians(0.76986 ), math.radians(1.76917 )]             # Inclination, Radians (Degrees)
        self.POMEGA = [math.radians(48.33167), math.radians(76.68069),
                       math.radians(-11.26064), math.radians(49.57854),
                       math.radians(100.55615), math.radians(113.71504),
                       math.radians(74.22988), math.radians(131.72169)]             # Longitudinal Ascending Node, Radians (Degrees)
        self.PPI = [math.radians(77.45645), math.radians(131.53298),
                    math.radians(102.94719), math.radians(336.04084),
                    math.radians(14.75385), math.radians(92.43194 ),
                    math.radians(170.96424), math.radians(44.97135)]            # Longitudinal Perihelion, Radians (Degrees)
        self.PL0 = [math.radians(252.25084), math.radians(181.97973),
                    math.radians(100.46435), math.radians(355.45332),
                    math.radians(34.40438), math.radians(49.94432),
                    math.radians(313.23218), math.radians(304.88003)]            # Mean Longitude, Radians (Degrees)
        self.PEDaysYr = [87.968, 224.695, 365.242, 686.973,
                        4330.595, 10746.94, 30588.740, 59799.9]           # Year, Earth Days
        self.PRadius_km = [2439.7, 6051.8, 6371.0, 3389.5,
                          69911, 58232, 25362, 24622]            # Radius, km
        print("\nCelestial Object Library successfully initialized")

    def values(self, category, which):

        if category == "Planets":

            for i in range(0, len(self.Planets), 1):

                if which == self.Planets[i]:

                    a = self.Pa[i]
                    e = self.Pe[i]
                    inc = self.Pi[i]
                    OMEGA = self.POMEGA[i]
                    PI = self.PPI[i]
                    L0 = self.PL0[i]
                    EDaysYr = self.PEDaysYr[i]
                    Radius_km = self.PRadius_km[i]

                    print("\nMercury Orbital Parameters accessed")

                    return a, e, inc, OMEGA, PI, L0, EDaysYr, Radius_km
