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
        t = second_line[1]

        for line in lines[1:]:
            if parsing_edges:
                string_integers = line.split(' ')
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

            if parsing_nodes:
                node = line.split(' ')
                red = (node.length > 1)
                nodes.add(node[0], Node(red))
                node_counter += 1
                if node_counter == total_nodes:
                    parsing_nodes = False
                    parsing_edges = True
                continue

    return nodes

'''Parse end'''

'''Helper methods'''

class Node:
    def __init__(self, red):
        self.red = red
        #self.id = node_id_string
        self.edges_out = {}
        self.edges_in = {}

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
