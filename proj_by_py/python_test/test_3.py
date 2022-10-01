'''
with open ("test_2.txt","r") as my:
    for line in my.readlines():
        print(line[:-1])
'''
#fifirst_name = list()
#profesion = list()
def parse_person_list_from_file():
 with open ("test_2.txt","r") as test:
    fifirst_name = list()
    print(test,"--")
    fifirst_name.extend(test.readlines())
    for i in fifirst_name:
       # print(i[:-1])
        fifirst_name.append(i)
 return fifirst_name

print(parse_person_list_from_file())
    
