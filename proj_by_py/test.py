


class person:

    def __init__(self,arry1):
        self.name = arry1[0]
        self.last_name = arry1[1]
        self.age = arry1[2]
        self.profession= arry1[3]

file_path = "1.txt"
def parse_person_list_from_file(file_path):
    person_list = []
    with open (file_path,"r") as fi:
        for i in fi:
            person_list.append(person( i.rstrip().split(",")))
            return person_list
persons = parse_person_list_from_file(file_path)
def filter_by_age_and_profession(persons, age, profession):
    res = str()
    age = int()
    profession = str(profession)
    for j in persons:
        if int(j.age )>= int(age) and j.profession == profession:
            res += j.name
            res += ", "
        return res
print(parse_person_list_from_file(file_path))
#print(filter_by_age_and_profession(persons, 30,"barman"))