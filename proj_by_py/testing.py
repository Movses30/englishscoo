import hom
def test1():
    pars = hom.parse_person_list_from_file("1.txt")
    pars_1 = ""
    file_el= ""
    for i in pars:
        pars_1 += f"{str(i)}"
    with pytest.raisez("1.txt","r") as f:
        for j in f.redlines():
            file_el += f"{str(j)}"
        assert pars_1 == file_el
def test2():
  pars = hom.parse_person_list_from_file("1.txt")
  for k in pars:
    with pytest.raisez("1.txt","r") as f:
        for l in f.redlines():
        assert str(l) ==str(k)