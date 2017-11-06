
from main import *

(nodes_1, s1, t1, c1, n1, e1) = parse_red_file("../data/common-1-20.txt")
(nodes_2, s2, t2, c2, n2, e2) = parse_red_file("../data/common-1-100.txt")
(nodes_3, s3, t3, c3, n3, e3) = parse_red_file("../data/increase-n8-1.txt")



def test_parse_common_1_20():
	assert nodes_1["purls"].red == True

def test_parse_common_1_20_2():
	assert nodes_1["brook"].red == False

def test_parse_common_1_100():
	assert nodes_2["start"].red == False

def test_parse_common_1_100_2():
	assert nodes_2["ender"].red == True

def test_parse_common_1_100_3():
	assert s2 == "start"

def test_parse_common_1_100_4():
	assert t2 == "ender"

def test_parse_common_1_100_4():
	assert "waged" in nodes_2["waled"].edges_out

def test_parse_common_1_100_5():
	assert "wooed" in nodes_2["cooed"].edges_in

def test_parse_increase_n8_1():
	assert "15" in nodes_3["2"].edges_out

def test_parse_increase_n8_1_2():
	assert "2" not in nodes_3["15"].edges_out 

def test_parse_increase_n8_1_3():
	assert c3 == 6

def test_parse_increase_n8_1_4():
	assert e3 == 16
