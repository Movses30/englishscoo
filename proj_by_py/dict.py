'''Գրել ֆունկցիա, որը կստուգի string-ը pangram է, թե՝ ոչ։

Note : Pangram-ը բառ կամ նախադասություն է, որը ներառում է այբուբենի
 բոլոր տառերը առնվազն 1 անգամ։
Օրինակ՝ "The quick brown fox jumps over the lazy dog"'''

a = input(":")
b = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
c = b.split()
if len(a) >= 25:
    print(a)
    if a is c:
      print(a,"---",c)
else:
    print("no")

