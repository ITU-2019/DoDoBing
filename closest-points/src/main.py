'''Imports'''
import sys
import math

from operator import itemgetter

import re


'''Fields'''
pairs_to_index = {}

'''fields End.'''

''' Parse file to internal data structure.
    @param: filename: The path of file to parse
'''

def parse_file(filename):
    data = ""
    n = 0
    header_ended = False
    full_regex = r'[\b\s]*(\d+)[\b\s]+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)[\b\s]+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)'
    points = []
    if filename.find("-tsp"):
        header_ended = True
    with open(filename) as f:
        data = f.readlines()
        point_index = 0
        for line in data:
            if(header_ended):
                match_obj = re.match(full_regex, line)
                if match_obj:
                    pairs_to_index[(float(match_obj.group(2)),float(match_obj.group(3)))] = point_index
                    point_index += 1
                    points.append((float(match_obj.group(2)),float(match_obj.group(3))))
            else :
                # check if header is finishing this line.
                if line.strip() == "NODE_COORD_SECTION":
                    header_ended = True

    return points

'''The passing file code. END'''

''' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Helper functions
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

def sort_points_into_x(points):
    return sorted(points,key=itemgetter(0))

def sort_points_into_y(points):
    return sorted(points,key=itemgetter(1))

def find_closest_pair_of_points(points):
    closest_pair = None
    closest_dist = float('inf')
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            if i != j:
                point_pair = (point1,point2)
                current_dist = dist(point_pair)
                if closest_dist > current_dist:
                    closest_pair = point_pair
                    closest_dist = current_dist
    return closest_pair

def dist(point_pair):
    point1, point2 = point_pair
    return math.sqrt(math.pow(point1[0]-point2[0],2.)+math.pow(point1[1]-point2[1],2.))


''' Parse file to internal data structure.
    @param: points_x_sorted: The x sorted points.
    @param: points_y_sorted: The y sorted points.
    @param: split_x: the splitting axis. If true split on x axis, if false split on y.
    @return: (Qx, Qy, Rx, Ry).
'''
def divide_sets(points_x_sorted, points_y_sorted, split_x):
    splitting_point = int(len(points_x_sorted)/2)

    if split_x:
        Qx = points_x_sorted[:splitting_point]
        Rx = points_x_sorted[splitting_point:]
        Qy = sort_points_into_y(Qx)
        Ry = sort_points_into_y(Rx)
        return (Qx, Qy, Rx, Ry)
    else:
        Qy = points_y_sorted[:splitting_point]
        Ry = points_y_sorted[splitting_point:]
        Qx = sort_points_into_x(Qy)
        Rx = sort_points_into_x(Ry)
        return (Qx, Qy, Rx, Ry)


def get_largest_value(points_x_sorted, points_y_sorted, split_x):
    if split_x:
        return points_x_sorted[-1][0]
    else:
        return points_y_sorted[-1][1]

def get_points_in_range(points_x_sorted, points_y_sorted,minimum_distance, split_value,split_x):
    min_val = split_value - minimum_distance
    min_index = None
    max_val = split_value + minimum_distance


    if split_x:
        for i, point in enumerate(points_x_sorted):
            if point[0] > min_val and min_index is None:
                min_index = i
            if point[0] > max_val:
                return points_x_sorted[min_index : i]
    else:
        for i, point in enumerate(points_y_sorted):
            if point[1] > min_val and min_index is None:
                min_index = i
            if point[1] > max_val:
                return points_y_sorted[min_index : i]

def sort_points_in_other_direction(potential_points, split_x):
    if split_x:
        return sort_points_into_x(potential_points)
    else:
        return sort_points_into_y(potential_points)

def get_closest_pair_in_potential_subset(potential_points_sorted):
    '''
    for each point in s compute distance to each of the next 15 points
    retun lowest distance.
    '''
    counter = 0
    closest_pair = None
    closest_dist = float('inf')
    for i in range(len(potential_points_sorted) -1):
        for j in range(i + 1, min(len(potential_points_sorted) -1, i + 15)):
            point_pair = (potential_points_sorted[i],potential_points_sorted[j])
            current_dist = dist(point_pair)
            if(closest_dist > current_dist):
                closest_pair = point_pair
                closest_dist = current_dist

    return closest_pair

def output_closest_pair(number_of_nodes, closest_pair):
    print("{0:2d} {1:.12f} --- {2:g} {3:g}".format(number_of_nodes, dist(closest_pair), pairs_to_index[closest_pair[0]], pairs_to_index[closest_pair[1]]))

''' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Helper Functions End
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

'''Algorithm'''
def closest_pair(points):
    points_x_sorted = sort_points_into_x(points)
    points_y_sorted = sort_points_into_y(points)
    return closest_pair_rec(points_x_sorted,points_y_sorted, True)

def closest_pair_rec(points_x_sorted, points_y_sorted, split_x):
    if len(points_x_sorted) <= 3:
        return find_closest_pair_of_points(points_x_sorted)

    (Qx,Qy,Rx,Ry) = divide_sets(points_x_sorted,points_y_sorted, split_x)
    closest_pair_in_q = closest_pair_rec(Qx,Qy,not(split_x))
    closest_pair_in_r = closest_pair_rec(Rx,Ry,not(split_x))
    minimum_distance = min(dist(closest_pair_in_q), dist(closest_pair_in_r))

    if minimum_distance != 0:
        split_value = get_largest_value(Qx,Qy,split_x)
        potential_points = get_points_in_range(points_x_sorted, points_y_sorted,minimum_distance, split_value,split_x)
        if potential_points:
            potential_points_sorted = sort_points_in_other_direction(potential_points, not(split_x))
            closest_pair_in_potential_points = get_closest_pair_in_potential_subset(potential_points_sorted)
            if closest_pair_in_potential_points and dist(closest_pair_in_potential_points) < minimum_distance:
               return closest_pair_in_potential_points
    if dist(closest_pair_in_q) < dist(closest_pair_in_r):
        return closest_pair_in_q
    else:
        return closest_pair_in_r

'''Algorithm End'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        points = parse_file(args[1])
        closest_pair = closest_pair(points)
        output_closest_pair(len(points), closest_pair)
'''END CODE'''
