from lec3_my_mod import earth_mass as em
from lec3_my_mod import gravity_constant as G
from lec3_my_mod import sigma_steff_bolc as sigma

g = 500 * G / 10**2
print(g)

x = em * G * sigma
print(x)