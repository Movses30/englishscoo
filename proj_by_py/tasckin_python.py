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
#task 10 ognecin

'''
first_number = float(input("number1:"))
Arithmetic_operators = input("Arithmetic operators: +, -, *, /, **, //, %:")
second_number = float(input("number2:"))
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
    print(ArithmeticOperators[Arithmetic_operators])

'''
     
     #task 11
'''Գրիր ծրագիր, որտեղ 50-350 միջակայքում կտպվի այն թվերը, որոնք զույգ են, եւ
բաժանվում են 7-ի։


a , b = 50 , 350
c = 20
while a < b:
    a += 1
    if a % 2 ==0 and a % 7 ==0:
        print(a)

'''



#m tasks 12

'''Գրիր ծրագիր, որը կտպի 100-150 միջակայքի զույգ թվերը՝ հակառակ
հաջորդականությամբ։

b = 150
first_num = 100
while first_num < b:
    b -= 1
    if b % 2 == 0:
     print(b)
'''
# task 13
'''Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
 и возвращающую True, если оно простое, и False - иначе.

def is_prime(is_prime_num):
 
    if is_prime_num % 2 == 1:
     if is_prime_num > 0:
        if is_prime_num < 1000:
         return True
    else:
        return False       
print(is_prime(9))

'''

'''Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
Вернуть True, если такая дата есть в нашем календаре, и False иначе. 

def date(dey,mont,year): 
 if dey <= 31 and dey > 0:
   if mont <= 12 and mont > 0:
     if year > 0 :
       return True
     else:           # None veradarcnum e None folse i poxaren  ?????????????????????????????????????????????????????????????????
      print(False)
      return False
    
print(date(29,2,11992))
'''
# task 14
'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, 
которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
 В остальных случаях вернуть строку "Неизвестная операция".
'''
'''
def arithmetic(a,b,x):
    if x == "-": #and a == int() or a == float() and b == int() or float():
        return a - b
    if x == "+" :# a == int() or float():
        return a + b
    if x == "/" :# a == int() or float():
        return a / b
    if x == "*" :# a == int() or float():
        return a * b  
    else:
        return "error"

print(arithmetic(2,8,"-"))
'''
#????????????????????????????????????????????????????????????????????????????????????????????????
'''
18:36
File "/home/mos/Desktop/python/proj_by_py/tasckin_python.py", line 309, in arithmetic
    return a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
18:37
error  է տալիս բայց ես գրել էմ որ հակառակ դեպքւմ տպի
18:37
else:
        return "Неизвестная операция"
18:38
ով կա python ից լավ ՞՞՞՞'''



'''Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
которому этот месяц принадлежит (зима, весна, лето или осень).


def season(month_1):
   if month_1 > 0 and month_1 < 12:
    if month_1 <= 3:
        return "cmer"
    elif month_1 <=6:
        return "garun"
    elif month_1 <=9:
        return "amar"
    elif month_1 <=12:
        return "ashun"
    else:
        return "tenc amis chka"

print(season(6))
'''

# taask 15
'''
Напишите программу на Python для подсчета количества символов (частоты символов) в строке.  
Пример строки: google.com '
Ожидаемый результат: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 
'''
# ???????????????????????????????????????????????????????????????????????
#  *.fromkeys() Создайте новый словарь с ключами из итерации и значениями, установленными в значение.
#   *.set() Создайте неупорядоченную коллекцию уникальных элементов. չկրկնվող էլէմէնտ topule
'''
str_1 = "google.com"
count_1 = dict().fromkeys(set(str_1))

for i in count_1.keys():
    print(i)
    count_1[i] = str_1.count(i)


print(count_1) # ==  {'e': 1, 'g': 2, 'l': 1, 'o': 3, '.': 1, 'c': 1, 'm': 1}
'''
# task 16

'''Напишите программу на Python, которая принимает радиус круга от пользователя и 
вычисляет площадь.  
Пример вывода:г = 1,1
Площадь = 3.8013271108436504 
  S = π × r^^2 

r =float(input("print in radius:"))
s = 3.14 * r * r
print(s)
'''
# task 17

'''Напишите программу на Python, которая принимает имя и фамилию пользователя и печатает 
их в обратном порядке с пробелом между ними.
nameinUs = input("what is your name ?")
srnume = input("what is your frstname?")
print(nameinUs[::-1] +" "+srnume[::-1])

'''
#task 18

'''6. Напишите программу на Python, которая принимает от пользователя последовательность чисел,
 разделенных запятыми, и генерирует список и кортеж с этими числами.  
Примерные данные: 3, 5, 7, 23 


list_1 =input("ok")
liste = list_1.split(",")
tapyle = tuple(liste)
print("list :",liste)
print("topule :", tapyle)
'''

# task 19
'''Напишите программу на Python для отображения первого и 
последнего цветов из следующего списка.  
color_list = ["Красный", "Зеленый", "Белый", "Черный"] 

color_list = ["Красный", "Зеленый", "Белый", "Черный"] 
print(color_list[0::3])

'''
#   home worck
'''Գրել ծրագիր, որը էկրանին կտպի հետևյալ պատկերը (օգտագործել ցիկլեր)․

from math import radians


sinbul = "*"
res = ""

for i in  sinbul:
    for j in range(6): 
     res = i * j 
     print(res)
     
     '''
'''Տրված է list տիպի հետևյալ փոփոխականը․
my_list = [4, 2, 18, 6, 21, 5]
Գրել ծրագիր, որը կփոխարինի նրա էլեմենտների արժեքները իրենց խորանարդներով։'''


'''Գրել ծրագիր, որը օգտատիրոջից կստանա ամբողջ թիվ, և, ցիկլի միջոցով, առանց 
built in ֆունկցիաներ օգտագործելու կհաշվի թվի թվանշանների քանակը։


num = input("write numbr:")
count = 0
for i in  num:
   count += 1 
print(count)  

+'''
'''Տրված է հետևյալ list տիպի փոփոխականը․
nums = [1, -8, 2, 10, 6, -3, 4, -12, -15, 5, 6]
Հաշվել այդ փոփոխականի բացասական արժեքով տարրերի միջին թվաբանականը։

res_len = 0
res =0
nums = [1, -8, 2, 10, 6, -3, 4, -12, -15, 5, 6]
for i in  nums:
    if i < 0:
     res += i 
     res_len += 1
     res / res_len

print(res / res_len)

'''




'''Օգտատերը մուտքագրել է string: Գրել ծրագիր, որի արդյունքում ցիկլը կընդհատվի, 
եթե տրված string-ի էլեմենտներից որևէ մեկը սիմվոլ (%, ^, &, @, !, etc.) լինի 
(կարելի է օգտագործել դրանց թվային արժեքները)։
my_str = input("print string:")
sinbul = ["%", "^", "&", "@", "!"]
for i in my_str:
    for j in sinbul:
        if i == j:
            break
                                          ??????????????????????????????????????????????????????????????????????????????
print(f"արգելված նսան չկա {my_str} ի մեջ ))")


a = int(input("input number:"))
my_list =[]
while a > 0:
    a = a / 2
    a - 1
    if a % 2 == 0:
        a - 1
        my_list.append(0)
    else:
        my_list.append(1)
    #a = a / 2
print(my_list)
'''

'''

x = input("print number:")
x = int(x)
for i  in range(10):
    res = x * i
    print(f"{x} x {i} = {res}")# f "{}" տպել եմ քրժեները 
    '''
'''
my_number = int(input()) 
 
my_binarry = ''  # ստեղծուն ենք փոփխ str "" 
 
while my_number > 0: # ցիկլին տալիս ենք պաըման 
    my_binarry = str(my_number % 2) + my_binarry #my_binarry ին վերագրում ենք my_number ը բաժանած(%) 2 + ""
    my_number = my_number // 2 # ստանւմ ենք ամբողջ մասը 14 // 8 == 1
 
print(my_binarry)
print(14 // 8)'''
'''
to_print="*****"
index=0
n=1
while index < 5:
    to_print_1=to_print[index]* n
    print (to_print_1.rjust(5," "))
    index += 1
    n+=1

'''
'''Գրել ֆունկցիա, որը որպես արգումենտ կստանա list և կվերադարձնի list-ի տարրերի գումարը

my_listsum = 0
def my_list_addfunc (x):
    for i in x:
        global my_listsum
        my_listsum += i 
    return my_listsum
        
print(my_list_addfunc(x = [5,7,8,9]))

#print(my_listsum)
'''

'''Գրել ֆունկցիա, որը որպես արգումենտ կստանա string և կտպի string֊ը շրջված։
def my_str_revers_func(str1):
   return str1[::-1]
print(my_str_revers_func("movses seyranyan"))

count_1 = 0
add_arg = 0
def sum_args_func(*args):
    global add_arg , count_1
    for i in args:
        add_arg += i
        if i:
            count_1 += 1
        print(count_1)
    return add_arg / count_1
print(sum_args_func(1,2,3,99,98))

''' # 1 1 2 3 5 8 13 21 34 55

'''Գրել ֆունկցիա , որը կտպի Ֆիբոնաչիի հաջորդականությունը մինչև n-րդ անդամը



def fibanachi(number):
    # քանի որ ֆիբ հաջորդականւթյան մեջ յոըրաքանչըուր հաջորդ թիվ նախորդ երկուսի գումարն է 
    # մեզ պետք է երկու փոփոխական որոնք իրենցից կներկայացնեն նախ ֆիբ առաջին երկու թվերը <<1,1>>  
    # հետո ամեն իտեռացիաց հետո արժեքները կփոխարինվի իր հաջորդ թվով 
    
    fib1 = 1 
    fib2 = 1  
    print(fib1,fib2,end=" ") # 
    while number > 2: # F(n) = F(n-1) + F(n-2) ֆիբանա(թիվ)(55) = ֆիբթիվ(նախորդ թիվ)(34) + ֆիբթիվ(նախորդի նախորդ)(21) 
        temp = fib2 
        fib2 = fib1 + fib2
        fib1 = temp
        number -= 1 
        print(fib2,end=" ")
        
print(fibanachi(10))
'''


'''Գրել ֆունկցիա, որը արգումենտում կստանա integer, կբազմապատկի տրված թվի
 թվանշանները իրար այնքան ժամանակ, քանի դեռ արդյունքը 
չի ստացվել միանիշ թիվ։ Վերադարձնել ստացված արդյունքը և տպել։


def gi(number):
  if number > 0 and number < 10:
    return number
  res = 1
  my_list = [] #for i in f:
  while number > 0:

    my_float = number  % 10
    number = number // 10
    my_list += [my_float] 
  for i in  my_list:
    res *= i
  
  return gi(res)
 
print(gi(90))

'''

'''Գրել ֆունկցիա, որը կստանա n քանակի արգումենտ (integer տեսակի) և կվերադարձնի
 այդ արգումենտների գումարի բացարձակ արժեքը
 (չօգտագործել sum(), abs() build-in ֆունկցiաները)։

def sum(*integer):
    res = 0
    for i in integer:
        res += i
    if res < 0:
        return -res 
    else:
        return res
print(sum(1,2,4,-8))

'''
'''

 Գրել ֆունկցիա՝ decoder, որը որպես արգումենտ ստանում է բինարի (երկուական համակարգով) տեքստ և 
 վերափոխում է սովորական/ընթեռնելի տեսքտի։ Սովորական տեքստի յուրաքանչյուր տառ, սիմվոլ 1 բայթ է = 8 բիթ:
'''
from symtable import Symbol


binary_text = "0101011101101000011001010110111000100000010010010010000001110111011100100110111101110100011001010010000001110100011010000110100101110011001000000110001101101111011001000110010100101100001000000110111101101110011011000111100100100000010001110110111101100100001000000110000101101110011001000010000001001001001000000111010101101110011001000110010101110010011100110111010001101111011011110110010000100000011101110110100001100001011101000010000001001001001000000110010001101001011001000010111000100000010011100110111101110111001000000110111101101110011011000111100100100000010001110110111101100100001000000110101101101110011011110111011101110011"


'''100               ^                     011        =        111
  4                                        3                       7
(0*2) + 1 =1            (0*2) + 0 = 0         (0*2)+1=1
(1*2) + 0 = 2            (0*2)+ 1 =1          (1*2)+1 = 3
(2* 2)+ 0 = 2            (1*2)+1 = 3           (3*2)+1 = 7'''

def binary_to_decimal(binaa):
    res =0
    for i in binaa : 
        res = (res * 2 ) + int(i)
    return res


def decod(binary_text):
    result_text = ""
    start_index = 0
    end_index = 8
   # print(binary_text[start_index:end_index])
    while start_index < len(binary_text):
        binary_symbol = binary_text[start_index:end_index]
        decimal_value = binary_to_decimal(binary_symbol)
        symbol = chr(decimal_value)
        result_text += symbol
        start_index += 8
        end_index += 8    
    return result_text
        

print(decod(binary_text))   
