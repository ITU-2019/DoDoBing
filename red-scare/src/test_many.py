from main import *


(nodes1, s1, t1, c1, n1, e1) = parse_red_file("../data/common-1-20.txt")
def test_common_1_20_many():
    assert m(nodes1,s1,t1,c1,e1) == '-'

(nodes2, s2, t2, c2, n2, e2) = parse_red_file("../data/common-1-100.txt")
def test_common_1_100_many():
    assert m(nodes2,s2,t2,c2,e2) == '-'

(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
def test_G_ex_many():
    x = m(nodes3,s3,t3,c3,e3)
    assert x == 2

(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
def test_wall_z_3_many():
    x = m(nodes4,s4,t4,c4,e4)
    assert x == 0

(nodes5, s5, t5, c5, n5, e5) = parse_red_file("../data/increase-n8-1.txt")
def test_increase_n8_1_many():
    x = m(nodes5,s5,t5,c5,e5)
    assert x == 2
