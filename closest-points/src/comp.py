import sys
import re


def comp(filename):
    data = ""
    n = 0
    points = []
    full_regex = r'^[\w\W]+:[\s]+[\d]+[\s]+([\d]+[\.]?[\d]*)$'
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            match_obj = re.match(full_regex, line)
            if match_obj:
                points.append((float(match_obj.group(1))))

    return points

def comparr(x1, x2):
    for index in range(len(x1)):
        v1 = x1[index]
        v2 = x2[index]
        diff = abs(v1-v2)
        if diff > 0.1 :
            print("Error test nr. --> ", index+1, " -- ", diff)

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        x1 = comp(args[1])
        x2 = comp(args[2])
        comparr(x1, x2)
'''END CODE'''
