


#dict_vreble = {"jon":2500,"mos":1200};  # inchpes mek hramani mijocov poxel mi qani <<keyeri arjeq>>    dict_vreble.ubdate({"jon":10000,"mos":50000});
'''inchpes poxel indexi arzheq@   asenq 
jon:2500
dict_vreble["jon"] = 2220
print(dict_vreble["jon])  ===  2220    '''
#dict_vreble["jon"] = 2220
#print(dict_vreble["jon"])
#print(dict_vreble["m"]) #KeyError: 'm'
# print(dict_vreble)
#dicte ={
 #   "bois":["mos","gago","hakop"],  # inchpes ave;lacnenq <<boisi>> mej nor arjeq    dicte["bois"].append("valod")
  #  #print(dicte.keys())         ===            ({"bois","girls"})
    #print(date2.values())   ===   {["ani","ina","haykuhui",mos","gago","hakop"]}
   # "girls":["ani","ina","haykuhui"] # kanchelu hamar print(dicte[])
#}


#print(dict_vreble)# == mos
# print(dict_vreble.get("noKey")) # kveradarcni vor chka key ayl voch te error  *.get("anhayt_key")=== none 
#print(dict_vreble["mos"])
#'''

'''Տրված է հետևյալ dictionary տիպի փոփոխականը․ 
my_dict = {2: 8, 5: 20, 3: 15, 6: 2, 11:20}: 
Հաշվել key-երի արժեքների գումարը։ '''

my_dict = {2: 8, 5: 20, 3: 15, 6: 2, 11:20}
res = 0
for i in my_dict.values():
    res = res + i
    1 + i
print(res)

