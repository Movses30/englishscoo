
import hom as ll


def test1():
    pars = ll.parse_person_list_from_file("1.txt")
    pars_1 = ""
    file_el= ""
    for i in pars:
        pars_1 += f"{str(i)}"
    
    with open("1.txt","r") as f:
        for j in f.readlines():
            file_el += f"{str(j)}"
        print(file_el)
        assert pars_1 == file_el
def test2():
  parse = ll.parse_person_list_from_file("1.txt")
  ff = ""
  kk= ""
  for k in parse:
    kk +=  f"{str(parse[k])}"
    print(kk,"---")   
    with open("1.txt","r") as y:
        for l in y.readlines():
            ff += f"{str(l)}"
            #print(ff,"+++")
        assert(ff) ==(kk)

test1()
#test2()


