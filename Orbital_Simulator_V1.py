# ------------------------- File Header -------------------------
# Author:           Daniel Ellis
# Last Updated:     2/21/2021
# Description:
# ----------------------------- End -----------------------------

from celestial_object import celestial_object
from celestial_object_library import celestial_object_library
from Orbit_Plotter_3D import Orbit_Plotter_3D

import matplotlib.pyplot as plt

celestial_object_library = celestial_object_library()
[a_mercury, e_mercury, i_mercury, OMEGA_mercury, PI_mercury, L0_mercury, EDaysYr_mercury, Radius_km_mercury] = celestial_object_library.values("Planets", "Mercury")
[a_venus, e_venus, i_venus, OMEGA_venus, PI_venus, L0_venus, EDaysYr_venus, Radius_km_venus] = celestial_object_library.values("Planets", "Venus")
[a_earth, e_earth, i_earth, OMEGA_earth, PI_earth, L0_earth, EDaysYr_earth, Radius_km_earth] = celestial_object_library.values("Planets", "Earth")
[a_mars, e_mars, i_mars, OMEGA_mars, PI_mars, L0_mars, EDaysYr_mars, Radius_km_mars] = celestial_object_library.values("Planets", "Mars")
[a_jupiter, e_jupiter, i_jupiter, OMEGA_jupiter, PI_jupiter, L0_jupiter, EDaysYr_jupiter, Radius_km_jupiter] = celestial_object_library.values("Planets", "Jupiter")
[a_saturn, e_saturn, i_saturn, OMEGA_saturn, PI_saturn, L0_saturn, EDaysYr_saturn, Radius_km_saturn] = celestial_object_library.values("Planets", "Saturn")
[a_uranus, e_uranus, i_uranus, OMEGA_uranus, PI_uranus, L0_uranus, EDaysYr_uranus, Radius_km_uranus] = celestial_object_library.values("Planets", "Uranus")
[a_neptune, e_neptune, i_neptune, OMEGA_neptune, PI_neptune, L0_neptune, EDaysYr_neptune, Radius_km_neptune] = celestial_object_library.values("Planets", "Neptune")

mercury_object = celestial_object(a_mercury, e_mercury, i_mercury, OMEGA_mercury, PI_mercury, L0_mercury, EDaysYr_mercury, Radius_km_mercury)
venus_object = celestial_object(a_venus, e_venus, i_venus, OMEGA_venus, PI_venus, L0_venus, EDaysYr_venus, Radius_km_venus)
earth_object = celestial_object(a_earth, e_earth, i_earth, OMEGA_earth, PI_earth, L0_earth, EDaysYr_earth, Radius_km_earth)
mars_object = celestial_object(a_mars, e_mars, i_mars, OMEGA_mars, PI_mars, L0_mars, EDaysYr_mars, Radius_km_mars)
jupiter_object = celestial_object(a_jupiter, e_jupiter, i_jupiter, OMEGA_jupiter, PI_jupiter, L0_jupiter, EDaysYr_jupiter, Radius_km_jupiter)
saturn_object = celestial_object(a_saturn, e_saturn, i_saturn, OMEGA_saturn, PI_saturn, L0_saturn, EDaysYr_saturn, Radius_km_saturn)
uranus_object = celestial_object(a_uranus, e_uranus, i_uranus, OMEGA_uranus, PI_uranus, L0_uranus, EDaysYr_uranus, Radius_km_uranus)
neptune_object = celestial_object(a_neptune, e_neptune, i_neptune, OMEGA_neptune, PI_neptune, L0_neptune, EDaysYr_neptune, Radius_km_neptune)

Orbit_Plot = Orbit_Plotter_3D()
for k in range(1, 20, 1):

    time_start = 0.01 * (k - 10.0)
    time_end = 0.01*k
    time_step = 20

    mercury_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(mercury_object.xecliptic, mercury_object.yecliptic, mercury_object.zecliptic, 1, mercury_object.radius)

    venus_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(venus_object.xecliptic, venus_object.yecliptic, venus_object.zecliptic, 2, venus_object.radius)

    earth_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(earth_object.xecliptic, earth_object.yecliptic, earth_object.zecliptic, 3, earth_object.radius)

    mars_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(mars_object.xecliptic, mars_object.yecliptic, mars_object.zecliptic, 4, mars_object.radius)

    jupiter_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(jupiter_object.xecliptic, jupiter_object.yecliptic, jupiter_object.zecliptic, 5, jupiter_object.radius)

    saturn_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(saturn_object.xecliptic, saturn_object.yecliptic, saturn_object.zecliptic, 6, saturn_object.radius)

    uranus_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(uranus_object.xecliptic, uranus_object.yecliptic, uranus_object.zecliptic, 7, uranus_object.radius)

    neptune_object.orbit_creation(time_start, time_end, time_step)
    Orbit_Plot.update_plot(neptune_object.xecliptic, neptune_object.yecliptic, neptune_object.zecliptic, 8, neptune_object.radius)

    plt.draw()
    plt.pause(0.001)

#print("handle", Orbit_Plot.handle)
plt.show()


