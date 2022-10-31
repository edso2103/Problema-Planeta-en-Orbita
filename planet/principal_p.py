import planet_cy
import planet_py
import time

ini_time=time.time()
planet_cy.main()
fin_time=time.time()
time_cython=fin_time-ini_time

ini_time=time.time()
planet_py.main()
fin_time=time.time()
time_python=fin_time-ini_time

print("Cython",time_cython)
print("Python",time_python)
print("Cython es", time_python/time_cython," veces más rapido que Python")
