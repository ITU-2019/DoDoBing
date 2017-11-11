'''Imports'''
import sys

'''Parse'''
def parse_red_file(filename):
    nodes = {}
    node_counter = 0
    edge_counter = 0
    parsing_nodes = True
    parsing_edges = False

    with open(filename) as f:
        lines = f.readlines()

        first_line = lines[0].split(' ')
        total_nodes = int(first_line[0])
        total_edges = int(first_line[1])
        cardinality = int(first_line[2])

        second_line = lines[1].split(' ')
        s = second_line[0]
        t = second_line[1].rstrip()

        for line in lines[1:]:
            line = line.rstrip()
            if parsing_edges:
                string_integers = line.split(' ')
                if len(string_integers) > 2:
                    node_id_1 = string_integers[0]
                    edge_type = string_integers[1]
                    node_id_2 = string_integers[2]

                    if edge_type == "--":
                        nodes[node_id_1].add_edge_out(node_id_2)
                        nodes[node_id_1].add_edge_in(node_id_2)
                        nodes[node_id_2].add_edge_out(node_id_1)
                        nodes[node_id_2].add_edge_in(node_id_1)

                    elif edge_type == "->":
                        nodes[node_id_1].add_edge_out(node_id_2)
                        nodes[node_id_2].add_edge_in(node_id_1)

                    edge_counter += 1
                    if edge_counter == total_edges:
                        parsing_edges = False
                    continue
                else:
                    parsing_edges = False

            if parsing_nodes:
                node = line.split(' ')
                red = (len(node) > 1)
                nodes[node[0]] = Node(red)
                node_counter += 1
                if node_counter > total_nodes:
                    parsing_nodes = False
                    parsing_edges = True
                continue

    return (nodes,s,t, cardinality, total_nodes, total_edges)

'''Parse end'''

'''Helper methods'''

class Node:
    def __init__(self, red):
        self.red = red
        #self.id = node_id_string
        self.edges_out = set([])
        self.edges_in = set([])

    def add_edge_out(self, node_id_string):
        self.edges_out.add(node_id_string)

    def add_edge_in(self, node_id_string): 
        self.edges_in.add(node_id_string)   
    
    def __str__(self):
        pass

def output(file_name, number_of_nodes, results):
    pass
    

'''Helper methods end'''

'''Algorithm'''
#altenate
def a(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

#few
def f(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

#many
def m(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

# None
def n(nodes, start_node_id, end_node_id, cardinality, total_edges):
    if nodes[end_node_id].red:
        return '-'
    # steps dict
    path_steps = {}

    # visited nodes tracker
    visited_nodes = set([])

    # nodes queue
    queue = []

    queue.append(start_node_id)

    # empty start path, origin node has no before node (None)
    path_steps[start_node_id] = None
    visited_nodes.add(start_node_id)

    while queue:
        # dequeue firstmost node in queue
        cur_node = queue.pop(0)

        # iterate to all subnodes
        for node in nodes[cur_node].edges_out:
            # Last node, the end
            if node == end_node_id:
                path_steps[node] = cur_node
                # find and return length of path
                return get_full_path(path_steps, end_node_id)

            # check if node is red
            if nodes[node].red:
                continue

            # Check if we didn't visit node before
            if node not in visited_nodes:
                # enqueue node
                queue.append(node)
                path_steps[node] = cur_node
                visited_nodes.add(node)
    return '-'

#some
def s(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

''' Traceback the valid path from a certain nid, return length of path '''
def get_full_path(path_dict, nid):
    cur_path = []
    while path_dict[nid] != None:
        cur_path.append(nid)
        nid = path_dict[nid]
    # Append end node to make sure length is not (path-1) length
    #cur_path.append("0")
    return len(cur_path)

'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        file_name = args[1]
        nodes, start_node_id , end_node_id, cardinality, total_edges = parse_red_file(file_name)

        # index :
            # A = 0
            # F = 1
            # M = 2
            # N = 3
            # S = 4
        results = []


        # do the yes no thing for each type.
        run = []

        # read keyboard input for each algortithm.
        


        output(file_name, len(nodes), results)
'''END CODE'''
