'''Տրված է list տիպի հետևյալ փոփոխականը․
my_list = [4, 2, 18, 6, 21, 5]
Գրել ծրագիր, որը կփոխարինի նրա էլեմենտների արժեքները իրենց խորանարդներով։

my_list = [4, 2, 18, 6, 21, 5]
res =[]
for i in my_list:
    #print(i)
    my_list = i ** 3
    res.append(my_list)
print((res))'''

#--------------------------------------------------
'''Գրել ծրագիր, որը մուտքագրված int տիպի փոփոխականը կդարձնի երկուական համակարգի և կտպի։
my_number = int(input()) 
 
my_binarry = ''  # ստեղծուն ենք փոփխ str "" 
 
while my_number > 0:
    my_binarry = str(my_number % 2 ) + my_binarry
    my_number = my_number // 2
print(my_binarry)'''

#=======================================
''' 
Գրել ծրագիր, որը կտպի առաջին 20 հատ պարզ թվերը։



flag = 0
n = int(input('Enter whole number to check : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        flag = 1
        break
    i += 1
if n == 1:
    print('1 is neither prime nor composite')
elif flag == 0:
    print(n,' is a prime number.')
elif flag == 1:
    print(n,' is not a prime number.')'''

#------------------------------

