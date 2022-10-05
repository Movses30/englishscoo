from ast import main


class Person:
    def __init__(self, aray_list):
           self.first_name = aray_list[0]
           self.last_name = aray_list[1]
           self.age = int(aray_list[2])
           self.profession = aray_list[3]
file_phat = "1.txt"
def file_path_open_create_list(file_path):
    person_list = []
    with open(file_path,"r") as f:
        for i in f.readlines():
            i = i.strip().split(',')
            person_list.append(Person(i))
        return person_list
persons = file_path_open_create_list(file_phat)
def filter_by_age_and_profession(persons, age, profession,) :
        res = str()
        age = int(age)
        profession = str(profession)
        for j in range(len(persons)):
             if persons[j].age >= int(age)and persons[j].profession == profession:
                res += persons[j].first_name
                res += ","
        return res
if __name__ == "__main__":
    main()
