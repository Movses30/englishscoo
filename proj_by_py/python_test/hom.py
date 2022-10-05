class Person:
    
    def __init__(self, my_arry):
           self.first_name = my_arry[0]
           self.last_name = my_arry[1]
           self.age = my_arry[2]
           self.profession = my_arry[3]


file_path = "1.txt"
def parse_person_list_from_file(file_path):
    persons = []
    with open(file_path,"r") as f:
        for i in f.readlines():
            persons.append(Person(i.strip().split(',')))
           
        return persons
persons = parse_person_list_from_file(file_path)
def filter_by_age_and_profession(persons, age, profession,) :
        res = str()
        age = int(age)
        profession = str(profession)
        for j in persons:
            if int(j.age) >= int(age )and j.profession == profession:
                res += j.first_name
                res += ", "
        return res

