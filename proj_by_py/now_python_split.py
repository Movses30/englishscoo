'''Գրել ֆունկցիա, որը կստուգի string-ը pangram է, թե՝ ոչ։

Note : Pangram-ը բառ կամ նախադասություն է, որը ներառում է այբուբենի բոլոր տառերը առնվազն 1 անգամ։
Օրինակ՝ "The quick brown fox jumps over the lazy dog"'''

str_1 = "The quick brown fox jumps over the l dog "

flag = True # ֆլագ վերագրել եմ True
def Pangram():
 alphabet = "abcdifghijklmnopqrstuvweyz"

 flag = True
 for char in alphabet: # ցիկլով ստւգել եմ բոլոր էլեմենտները  alphabet ի 
    if char not in str_1.lower(): # եթե  alphabet ի էլեմենտներից չկա str_1.lower() փոքրատառ str_1 ի մեջ 
        flag = False     # ֆլագին վերագրի False

 if (flag == True): # եթե ֆլագս true տպի pangram
    print("pangram")
 else: # else "not pragman"
    print("not Pangram")      

Pangram()