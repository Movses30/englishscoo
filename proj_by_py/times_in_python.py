from datetime import datetime
from time import ctime, time, sleep, asctime, localtime
from random import random
'''
seconds = time() # seconds in 01.01.1970 ear
print(ctime(seconds)) # now time

'''
'''
for i in range(100):
    print(i)
    sleep(1)
#tpum e mekic minchev 99 tver@ 1 varikyan @ndmichumov
'''
print(asctime()) # Wed Sep  7 15:37:18 2022
print(localtime()) # time.struct_time(tm_year=2022, tm_mon=9, tm_mday=7, tm_hour=15, tm_min=39, tm_sec=14, tm_wday=2, tm_yday=250, tm_isdst=0)
print(localtime().tm_year)