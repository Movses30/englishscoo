
class persiom:
    def __init__(self, my_array):
            self.first_name = my_array[0]
            self.last_name = my_array[1]
            self.age = int(my_array[2])
            self.profession = my_array[3]
file_path = "1.txt"
def file_path_open_create_list(file_path):
    person_list = []
    with open(file_path,"r") as f:
        for i in f.readlines():
            i = i.strip().split(',')
            person_list.append(persiom(i))
        return person_list
persons = file_path_open_create_list(file_path)
def filter_by_age_and_profession(persons, age, profession,) :
        res = str()
        age = int(age)
        profession = str(profession)
        for j in range(len(persons)):
             if persons[j].age >= int(age)and persons[j].profession == profession:
                res += persons[j].first_name
                res += ","
        return res
print(filter_by_age_and_profession(persons,20,"barman"))


