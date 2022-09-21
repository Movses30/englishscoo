'''


str_ex = "Computer Name"

#print(len(str_ex))
#print(str_ex[6:15])
#print(str_ex[7:])
item = "Computer Name"
#print(item[:-1:-12:-1])
#print(item.split())
#print(item.replace("Computer Name","computer name eman  retupmoc"))
#revers_itm = item[::-1]


print(item)
#print(revers_itm)
print(item.join(["i"]))
'''
'''
if x == "+" :# a == int() or float():
        return a + b
    if x == "/" :# a == int() or float():
        return a / b
    if x == "*" :# a == int() or float():
        return a * b  '''

binary_text = "0101011101101000011001010110111000100000010010010010000001110111011100100110111101110100011001010010000001110100011010000110100101110011001000000110001101101111011001000110010100101100001000000110111101101110011011000111100100100000010001110110111101100100001000000110000101101110011001000010000001001001001000000111010101101110011001000110010101110010011100110111010001101111011011110110010000100000011101110110100001100001011101000010000001001001001000000110010001101001011001000010111000100000010011100110111101110111001000000110111101101110011011000111100100100000010001110110111101100100001000000110101101101110011011110111011101110011"


        # def binary_to_decimal() ֆունկցիան երկուականը սարքում է տասնորդական 
def binary_to_decimal(binaa):
    res =0
    for i in binaa : 
        res = (res * 2 ) + int(i)
    return res


def decod(binary_text):
    result_text = ""    
    start_index = 0 # սահմանել հատված երկուական կոդը 8բիթ սարքելու համար
    #end_index = 8
    while start_index < len(binary_text):
        binary_symbol = binary_text[start_index:8 + start_index] # սահմանել հատված երկուական կոդը 8բիթ սարքելու համար
        decimal_value = binary_to_decimal(binary_symbol)
        symbol = chr(decimal_value)
        result_text = result_text + symbol
        start_index += 8
        #end_index += 8    
    return result_text
        

print(decod(binary_text))   
'''ստեղծել եմ ֆունկցիա որը հայտարարել եմ փոփոխականներ  
result_text =  ""  որտեղ կգցեմ իմ դեքոդ եղած նշանը
  start_index =   միջակայքի համար սկիզբ   
end_index =      միջակայքի համար վերջ
ստեղծել ցիկլ եվ բաժանել 8բիթերի մեր երկուականի թվերը
ցիկլի մեջ քանի դեռ մեր len(binary_text) > start_index 
հետո սարքել եմ տասական համակարգ հետո սարքել եմ սիմվոլ chr(decimal_value) ավելացնելով  esult_text  ի մեջ եվ վերադարձրել արդյունքը'''










