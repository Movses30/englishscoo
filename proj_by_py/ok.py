

def my_split(x):
    x = input("text:")
    symbols = "!?,.'\"`;():" # список возможных "лишних" символов
    for i in symbols: # перебор всех символов внутри строки symbols 
	    x = x.replace(i, " ") #замена текущего символа на пустое место
    return x
print(my_split(x="clkdv fm"))