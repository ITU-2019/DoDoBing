from main import *



def test_G_ex_many():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert t3 in nodes3[s3].edges_out


def test_5():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "5" in nodes3[s3].edges_out


def test_1():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "1" not in nodes3[s3].edges_out

def test_6():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "6" not in nodes3["5"].edges_out

def test_6_not_in_7():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "6" not in nodes3["7"].edges_out

def test_5_contains_7():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "7" in nodes3["5"].edges_out

def test_y_contains_7_in():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "7" in nodes3["5"].edges_in