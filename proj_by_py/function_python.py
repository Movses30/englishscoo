def bin_to_dec(digit):
  dlina=len(digit)
  print (dlina)
  chislo_dec=0
  for i in range(0, dlina):
    chislo_dec=chislo_dec+int(digit[i])*(2**(dlina-i-1))
    return chislo_dec
a=input("Введите двоичное целое число =")
print("Двоичное целое число",a,"соответствует десятичному числу ", bin_to_dec(a))