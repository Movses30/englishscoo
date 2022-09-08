'''
 #պետք է տպի ներմուծված թվի յոթնապատիկը
a = int(input())
a *=7
print(a)

'''
# task numbr 2
'''
a = float(input())
c = a*2
print(c)
#պետք է տպի ներմուծված թվի կրկնապատիկը
'''

#task  num 3

'''
Հաշվիր օգտագործողի տարիքը։ Օգտագործողը պիտի ներմուծի իր ծննդյան
թվականը, իսկ ծրագիրը պետք է տպի նրա տարիքը։




from time import ctime, time, sleep, asctime, localtime
usBrdey = input("write your birthyear") 
usBrdey1 = int(usBrdey)  # ogtagorcum enq int() vorpesi type lini tiv
current_year = localtime().tm_year  # localtime().tm_year  cuic e talis nekaic tarin  
current_year1 = int(current_year) 
useyear = current_year1- usBrdey1  
print(type(useyear))
print(useyear)
'''


# task 4



'''Օգտագործողը ներմուծում է որոշակի քանակի նիշեր(symbol), իսկ ծրագիրը
պետք է տպի դրա եռապատիկը։

symbol = input("write dymbol")
res = symbol * 3
print(res)
'''

# task 5



'''Օգտագործողը ներմուծում է օրերի քանակը, իսկ ծրագիրը պիտի տպի, թե տվյալ
քանակի օրերում քանի վայրկյան կա։
dey = int(input("write count day"))
cecDey = 24 * 60 * 60 * dey
print(cecDey)
'''

# task 6


'''Գրիր ծրագիր, որը կհաշվի 5/x^2 + x*y*z-z/x արժեքը, որտեղ x, y, z ներմուծում է
օգտվողը

x = int(input("input x"))
y = int(input("input y"))
z = int(input("input z"))
res = 5/(x**2) + (x * y * z) - (z / x )
print(res)
  '''


# task 7

'''Գրիր ծրագիր, որը կտպի օգտագործողի ներմուծած թիվը զու՞յգ է, թե՞ կենտ

num = input("write in number:")
num1 = int(num)
if num1 % 2 == 0:
        print("input nummber is even")
else:
    print(f"{num1} add number")
'''

# task 8


'''Գրիր ծրագիր, որը կտպի օգտագործողի ներմուծած թիվը միաժամանակ 2-ի եւ 3-
ի բազմապատի՞կ է, թե՞ ոչ։

i = input("")
inum = int(i)
num1 = 1874
num2 = 2232

if num1 % inum == 0 & num2 % inum == 0:
    print(f"{inum}@  bazmzpatiq e {num1} end {num2} hamar  ")
else:
    print(f"{inum} bazmzpatik che {num1} end {num2} hamar")
'''

# task 9


'''Պատկերացրու, որ ունես մի խանութ, որտեղ վաճառում ես ընդամենը 10
ապրանք։ Այդ ապրանքներից յուրաքանչյուրի ճշգրիտ անվանումը գրելից(կապ
չունի մեծատա՞ռ, թե՞ փոքրատառ) էկրանին պիտի տպվի ապրանքի գինը։
'''
#metode in loop for
'''
name_of_Produqt = input("")
produqt = {
    "kola":670,
    "potatoes":250,
    "bread":220,
    "egg":80,
    "milk":180
}
for a in produqt:
    if name_of_Produqt not in produqt:
        print("not is product")
        break
    if name_of_Produqt in produqt:
        print(produqt[name_of_Produqt])
        break
'''
#metode in while loop
'''while name_of_Produqt in produqt:
    if name_of_Produqt in produqt:
        print(produqt[name_of_Produqt])
        break
else:
    if name_of_Produqt not in produqt:
        print(f"{name_of_Produqt} not is product")
'''
#metode in if ifelse

'''
if product_name == "bread":
     print(produqt["bread"])
elif product_name == "kola":
     print(produqt["kola"])
elif product_name == "egg":
    print(produqt["egg"])
elif product_name == "milk":
    print(produqt["milk"])

elif product_name == "potatoes":
    print(produqt["potatoes"])
else:
    print("end")
'''
#----------

'''

    # task 10

Ստեղծիր հաշվիչ, որը կկատարի մաթեմատիկական գործողություններ հետեւյալ
օպերատորներով։ «+
 -
  *
   /
    **
     //
      %
      »
      '''
'''+ 	Addition 	x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	x / y 	
% 	Modulus 	x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division
'''
'''
print("Ноль в качестве знака операции"
      "\n]завершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':              ?????????????????????????????????????????????????
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
'''
#task 11 ognecin

'''first_number = int(input("number1:"))
Arithmetic_operators = input("Arithmetic operators: +, -, *, /, **, //, %:")
second_number = int(input("number2:"))
#ArithmeticOperators1 = ("+", "-", "*", "/", "**", "//", "%")
ArithmeticOperators = {
"+":(f"{first_number + second_number}"),
"-": (f"{first_number - second_number}"),
"*":(f"{first_number * second_number}"),
"**" :(f"{first_number ** second_number}")
}
if second_number == 0:
    if Arithmetic_operators == "/" or Arithmetic_operators == "//" or Arithmetic_operators == "%":
        print(" ZeroDivisionError: division by zero !!!")
    else:
        print(ArithmeticOperators[Arithmetic_operators])
else:
#version 2
#    ArithmeticOperators2 = {
#    "/":(f"{first_number / second_number}"),
#    "%" :(f"{first_number % second_number}"),
#    "//" :(f"{first_number // second_number}")
#    }
#    ArithmeticOperators.update(ArithmeticOperators2)
    ArithmeticOperators = {
        **ArithmeticOperators,
        **{
        "//":(f"{first_number // second_number}"),
        "/":(f"{first_number / second_number}"),
        "%":(f"{first_number % second_number}")
        }
    }
    print(ArithmeticOperators[Arithmetic_operators])'''


                                                             
