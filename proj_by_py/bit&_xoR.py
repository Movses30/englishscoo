flags = 4
mask =  3
resu = flags ^ mask   # 100 == 0100    4
print(resu)           #  11 == 0011    3
print(bin(resu))      # resu== 0111    7  