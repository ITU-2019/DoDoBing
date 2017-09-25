from main import *

def test_parse_count_points():
    points = len(parse_file("../data/att48-tsp.txt"))
    assert points == 48

    points = len(parse_file("../data/d2103-tsp.txt"))
    assert points == 2103

    points = len(parse_file("../data/rd100-tsp.txt"))
    assert points == 100

    points = len(parse_file("../data/kroA200-tsp.txt"))
    assert points == 200

    points = len(parse_file("../data/lin318-tsp.txt"))
    assert points == 318

def test_parse_count_points_huge():
    points = len(parse_file("../data/brd14051-tsp.txt"))
    assert points == 14051

def test_parse_int_points():
    points = parse_file("../data/a280-tsp.txt")
    pointsLen = len(points)

    assert pointsLen == 280
    assert points[21] == (148, 169)
    assert points[279] == (280, 133)

def test_parse_double_points():
    points = parse_file("../data/ch130-tsp.txt")
    pointsLen = len(points)

    assert pointsLen == 130
    assert points[10] == (280.7494438748, 5.9206392047) # 11th point, index offset
    assert points[78] == (280.5784506848, 458.7533546925)

def test_parse_special_points():
    points = parse_file("../data/d2103-tsp.txt")

    assert len(points) == 2103
    assert points[0] == (0.00000e+00, 0.00000e+00)
    assert points[32] == (1.14170e+03, 2.33630e+03)
