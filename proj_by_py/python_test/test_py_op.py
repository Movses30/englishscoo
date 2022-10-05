import mar_op  as mt


def test_tio ():
  a =mt.multi(3,4)
  assert a == 12


def test2():
  b = mt.sumi(10,1)
  assert b ==11
