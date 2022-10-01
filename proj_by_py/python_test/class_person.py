
class Person:
    def __init__(self,first_name,last_name,age,profession):
           self.first_name = first_name
           self.last_name = last_name
           self.age = age
           self.profession = profession
    
    def __str__(self):
        #file_phat = "test_2.txt"
        with open ("test_2.txt","r") as f:
            
            print(f.readlines)



de = Person("d","s","d","f")
print(de.__str__())







file_phath = "test_2.txt"