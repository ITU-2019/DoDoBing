from main import *

def test_get_next_unmatched_man_normal():
    arr = ["1", "2", "3", "4"];
    assert get_next_unmatched_man_id(arr) == "4"
    assert get_next_unmatched_man_id(arr) == "3"

def test_get_next_unmatched_man_empty():
    arr = [];
    assert get_next_unmatched_man_id(arr) == None
