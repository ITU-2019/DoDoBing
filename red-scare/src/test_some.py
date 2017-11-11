from main import *

(nodes_1, s1, t1, c1, n1, e1) = parse_red_file("../data/common-1-20.txt")
def test_common_1_20_some():
    assert s(nodes_1,s1,t1,c1,e1) == False

(nodes_2, s2, t2, c2, n2, e2) = parse_red_file("../data/common-1-100.txt")
def test_common_1_100_some():
    assert s(nodes_2,s2,t2,c2,e2) == False

(nodes_3, s3, t3, c3, n3, e3) = parse_red_file("../data/increase-n8-1.txt")
def test_increase_n8_1_some():
    assert s(nodes_3,s3,t3,c3,e3) == True