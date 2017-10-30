'''Imports'''
import sys

'''Parse'''
def parse_red_file(filename):
    nodes = []

    node_counter = 0
    edge_counter = 0


    parsing_nodes = False
    parsing_edges = False

    total_nodes = 0
    total_edges = 0
    pass
    ## TODO FIX THE PARSER ...
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if parsing_edges:
                string_integers = line.split(' ')
                node_id_1 = int(string_integers[0])
                node_id_2 = int(string_integers[1])
                capacity = int(string_integers[2])
                edges.append( Edge(node_id_1, node_id_2, capacity, flow))
                nodes[node_id_1].addEdgeTo(node_id_2, edge_counter)
                nodes[node_id_2].addEdgeTo(node_id_1, edge_counter)
                edge_counter += 1
                if edge_counter == total_edges:
                    parsing_edges = False
                continue
            if parsing_nodes:
                nodes.append(Node(line[:-1], node_counter))
                node_counter += 1
                if node_counter == total_nodes:
                    parsing_nodes = False
                continue
            if total_nodes == 0:
                total_nodes = int(line)
                parsing_nodes = True
                continue
            if total_edges == 0:
                total_edges = int(line)
                parsing_edges = True

    return(nodes,edges)

'''Parse end'''

'''Helper methods'''

class Node:
    def __init__(self, node_id_string):
        self.id = node_id_string
        self.related_edges = []

    def addEdgeTo(self, node_id_string):
        self.related_edges.append(node_id_string)
    
    def __str__(self):
        pass

def output(file_name, number_of_nodes, results):
    pass
    

'''Helper methods end'''

'''Algorithm'''
#altenate
def a(nodes, start_node_id, end_node_id):
    pass

#few
def f(nodes, start_node_id, end_node_id):
    pass

#many
def m(nodes, start_node_id, end_node_id):
    pass

#none
def n(nodes, start_node_id, end_node_id):
    pass

#some
def s(nodes, start_node_id, end_node_id):
    pass


'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        fine_name = args[1]
        nodes, start_node_id , end_node_id = parse_red_file(filename)

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
