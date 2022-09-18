'''familyMember = {}
qanak = int(input("Nermuceq Yntaniqi andamneri qanak@: "))
family = {}
i = 0
while i < qanak:
    name = input("ask name for family Member!")
    old = int(input("how old are famyily Member?"))
    familyMember[name] = old
    i = i + 1
    if(old > 0 and old <= 8):
        family["child"] = name
    if(old >= 9 and old <= 17):
        family["teenager"] = name
    if(old >= 18 and old <= 30):
        family["young"] = name
    if(old >= 30 and old <= 60):
        family["adult"] = name
print(family) 
# ղնդիրները ամբողջովին հասկանալով եմ լուծել
# մեծ սիրով կպատասղանեմ ձեր հարցերին տնաինի հետ կապված
# խնդրում եմ լինել ներողամիտ որոշ հարցեր առանց մեկնաբանության թողնելու համար
'''
'''
x = int(input("print number:"))
y = int(input("raise a  number to the power:"))


for i in range(x):# ցիկլը կկրկնի առաջին ներմւծաց թվի քանակությամբ 
    res = (x * y) # առաջին թիվը բազմապատկում է երկրորդ թվով /////  առջին ներմւծաց թվի քանակությամբ և վերագրւմ res փոփոխականին
print((res))   # տպում է res փոփոխականի արժեքը



animals_1 = {"dog", "cat", "pig", "horse", "lamb"}
animals_2 = {"pig", "sheep", "rabbit", "dog"}
#animals_3 = {i}



for i in animals_1 :
    animals_3 = {}
    #print(i)
    for j in animals_2:
     #   print(j)
        if i != j:
            animals_3.update([i])
print(animals_3)
'''

def sum(*integer):
    res = 0
    for i in integer:
        res += i
    if res < 0:
        return -res #  
    else:
        return res
print(sum(1,2,4,8))