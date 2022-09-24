
from operator import index
a = "     1 2 3 44 555 6666 77777  ",
#print(a.split())

def my_split(text,delimiter=None,coumt=None): # None եթե արժեք չունի
    lis_of_split = []  # 
    is_delimiter_None = False # ետե արժեք չունի ոչ
    if coumt == None:#  
        coumt = len(text)# քաւնտին վերագրի  տեքստի լենքը 
    if delimiter == None:  #  եթե նօն է 
        delimiter = " "# վերագրի բացատանիշ
        text = text.strip()# տեքստի բացատանիշերը ջնջի
        is_delimiter_None = True# վերագրի այո սարքիր դրական
    while len(lis_of_split) < coumt and delimiter in text: # մեկ ցիկլը ոգտագորցել եմ երեք արգւմենտների համար
        sub_string = text[:text.index(delimiter)] # [0:]index(delimite)== delimite ի ինդեքսին մետ տեքստի մեջ
        if is_delimiter_None:# Foles 
            lis_of_split.append(sub_string.strip())# բացատանիշերը ջնյիր ավելացրու lis_of_split ի մեյ
            text = text[text.index(delimiter)+len(delimiter):].strip()# կարա մեր index(delimite) ով չվերջանա string ը text ի մնացորդնել  strip() արա
        else:#
            lis_of_split.append(sub_string)#
        
            text = text[text.index(delimiter)+len(delimiter):]#
    lis_of_split.append(text) #պայմանը չբավարարելու դեպքւմ append արա մնացորդը texti մեջ
        
    return lis_of_split# վերադարցրու lis_of_split 
print(my_split("     1 2 3 44 555 6666 77777  ",None, 2))



    

'''Գրել  module , որը կունենա split() ֆունկցիա։ Ֆունկցիան պետք է  
նույնությամբ աշխատի, ինչպես string֊ի split()֊ը։ Այլ ֆայլից կանչել ֆունկցիան։ '''