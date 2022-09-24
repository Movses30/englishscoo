'''#names = ["Movses","Seyranyan","Mariam","Vahram"]
#print(names)
eges = ["30","33","36"]
#print(eges[2]) # >> =  36   tpir eges-i errord arzheq@ kam 2-rd index@ 
#print(eges[-1]) #>> = 36   tpir verjin indexi tak gtnvox arzheq@
#eges[0] = "gurgen"
#print(eges[0]) # eges[0] = "gurgen"  es poxeci indexi arzheq@ 
eges.append("true") # *.append("value") = avelacnel index ir arzheqov karox enq mek indeq i arzeq avelacnel
print(eges) # [30 33 36 true]

eges.pop() # jnjel verjin element@ *.pop()
print(eges) # == [30, 33, 36]
eges.pop(1) # jnjel koknkret index@
print(eges) # == [30 , 33 ] es pop(1) hramanov jnjeci 36@
lestelement = eges.pop() # ir mej pahum e verjin element@
print(lestelement) # == 36
'''
'''
sinbul = "*****"
res = ""  # փոփոխական որի մեջ ցիկլի 
# ամեն շրջանից հետո կավելանա եվս մեկ "*" նշան

for i in  sinbul: # i քնի կա  sinbul ի մեջ անցի հաջերդ տող։
    for j in range(6): # j ֊ին  6 անգամ ֆռա
     res = i * j  #  i == "*"    j ==  0,1,2,3,4,5   հերթով բազմապատկւմ է j ով  եւ գցում res ի մեջ
     print(res) # եւ տպում resի արժեքը ամեն ցիկլից հետո ։'''
''''''
'''Ստեղծել module, որը հաշվում է ֆունկցիային որպես արգումենտ փոխանցված list֊ի և tuple֊ի չկրկնվող տարրերի գումարը։
 Տվյալ ֆունկցիան կանչել մեկ այլ ֆայլից և տպել արդյունքը։


def sum_in_list_or_topule_unit_el(list_1,tuple_1):
    res=0
    for i in tuple_1:
        if i not in list_1: # եթե i չկա list_1 ի մեյ res+=i
                res+=i
    for j in list_1:
        if j not in tuple_1: # եթե j չկա tuple_1 ի մեյ res+=j
            res+=j
    return res   # վերադարցրւ res
#print(sum_in_list_or_topule_unit_el((1,2,3),[2,3,1]))
э'''


'''Տրված է եռանկյուն, որի կողմերն են՝
a = 14
b = 7
c = 10
Գրել ֆունկցիաներ, որոնցից մեկը կհաշվի տրված եռանկյան միջին գծերի երկարությունները, իսկ մյուսը՝ 
 դրանցով կազմված եռանկյան պարագիծը։ Ֆունկցիաները կանչել main()-ից։'''
from cmath import sqrt
if __name__ == "__main__":

 def par(a=14,b=7,c=10):
    res =a/2 + b/2 +c/2
    return res # պարագիծ հավասար է երեք կողմերի գւմարին 
 
def mijnagci(a=14,b=7,c=10):
  a= a/2
  b =b/2
  c= c/2
  return a,b,c
#if __name__ == "__main__":

#print("---",par()) # print կանի միայն այն ժամանակ երփ հենց այս կոդը կաշխատացնեմ,
#print("+++",mijnagci())