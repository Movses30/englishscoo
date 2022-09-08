first_number = int(input("first number:"))                                      
second_number = int(input("second number:"))
#ArithmeticOperators1 = ("+", "-", "*", "/", "**", "//", "%")

ArithmeticOperators = {
"+":(f"{first_number + second_number}"),
"-": (f"{first_number - second_number}"),
"*":(f"{first_number * second_number}"),
"/":(f"{first_number / second_number}"),
"%" :(f"{first_number % second_number}"),
"**" :(f"{first_number ** second_number}"),
"//" :(f"{first_number // second_number}"),
}
Arithmetic_operators = input("Arithmetic operators: +, -, *, /, **, //, %:")              
#ArithmeticOperators1 = ("+", "-", "*", "/", "**", "//", "%")

for Arithmetic_operators in ArithmeticOperators:
  if second_number == 0 and Arithmetic_operators == "/" or "//" or "%":
   print(" ZeroDivisionError: division by zero !!!")
   break
else:
   print(ArithmeticOperators[Arithmetic_operators]) 
