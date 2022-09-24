'''Գրել class, որը կունենա երկու մեթոդ՝ get_string և print_string։
 Առաջին մեթոդը օգտատիրոջից ստանում է string, երկրորդ մեթոդը տպում է 
 ներմուծած string֊ը մեծատառերով։ *
19 баллов


class Homework:
    def get_string(self):
        self.string_input = input() # self հղում եմ տվել դեպի string_input վօրին վերագրել եմ input() ֆունկցիան
        if self.string_input == str(): # ստուգել եթե բան չեն ներմւցել այսինքն ստրինգ չի նետմւցվաց վերադարցրու plis print string now:
            return "plis print string now:"
        else:
            return self.string_input
    def print_string(self): 
        #print(self.string_input.upper())
        return self.string_input.upper()  # get_string ի սելֆին սարքել եմ մեծատառ 

create = Homework()   # սարքել եմ օբյեկտ և կանչել այն 
print(create.get_string())
print(create.print_string())'''

#kkkkkkkkkkkkkkkkkkkkkkkk
'''Գրել Triangle անունով class, որը ստանում է երկու պարամետր՝ 
base (հիմք) և height (բարձրություն), և ունի մեկ մեթոդ, որը հաշվում է եռանկյան մակերեսը։'''


class Triangle:


    def __init__(self,base,height):
        
         self.base =base
         self.height = height
         #return (self.base * self.height) / 2
        
    def prim(self):
        return (self.base * self.height) / 2
des = Triangle(3,4)
print(des.prim())










































