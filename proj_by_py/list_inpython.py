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

lit2list = [
    [],  #incpes avelacnel value 0 indexin
    [1,2,3,4,5,6,7,8,9],
    ["m","o","vova","s","e","s"]
]
#print(lit2list[2][2]) #== vova
print(lit2list)
print("-------------------------------")
#lit2list.append("avelacav")
reslist = lit2list[0]+ lit2list[1]+ lit2list[2]
reslist.append("avelacav")
print(lit2list)
print(type(reslist))
