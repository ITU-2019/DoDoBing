from main import *

(nodes1, s1, t1, c1, n1, e1) = parse_red_file("../data/common-1-20.txt")
def test_common_1_20_alternate():
    assert a(nodes1,s1,t1,c1,e1) == False

(nodes2, s2, t2, c2, n2, e2) = parse_red_file("../data/common-1-100.txt")
def test_common_1_100_alternate():
    assert a(nodes2,s2,t2,c2,e2) == False

(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
def test_G_ex_alternate():
    assert a(nodes3,s3,t3,c3,e3) == True

