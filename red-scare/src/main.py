'''Imports'''
import sys
import argparse

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

def output(instance_name, nodes_len, a_res, f_res, m_res, n_res, s_res, latex):
    instance_name = instance_name.replace(".txt","").replace("../data/","") 

    res = "{:<20}".format(instance_name) + "|"
    res += "{:>8}".format(str(nodes_len)) + " |"
    res += "{:>6}".format(str(a_res)    ) + " |"
    res += "{:>6}".format(str(f_res)    ) + " |"
    res += "{:>6}".format(str(m_res)    ) + " |"
    res += "{:>6}".format(str(n_res)    ) + " |"
    res += "{:>6}".format(str(s_res)    )
    
    if latex:
        return res.replace("|", "&")
    else:
        return "|| " + res + " ||"

'''Helper methods end'''

'''Algorithm'''
#altenate
def a(nodes, start_node_id, end_node_id, cardinality, total_edges):
    visited = set([start_node_id])
    start_node = nodes[start_node_id]
    queue = [start_node]
    while len(queue) > 0:
        node = queue.pop() # this makes it DFS, if we use pop(0) its BFS.
        for node_id in node.edges_out:
            if node_id not in visited:
                if nodes[node_id].red != node.red: #if not the same colour
                    if node_id == end_node_id:
                        return True
                    queue.append(nodes[node_id])
                    visited.add(node_id)
    return False






#few
def f(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

class Path_node:
    def __init__(self, node_id, parent_path_node):
        self.node_id = node_id
        self.parent_path_node = parent_path_node
    
    def in_path(self, new_node_id):
        if new_node_id != self.node_id:
            if self.parent_path_node == None: # Root
                return False
            return self.parent_path_node.in_path(new_node_id)
        else:
            return True
    
    def reds_in_path_counter(self, nodes,  count):
        if nodes[self.node_id].red:
            if self.parent_path_node == None: # Root
                return count + 1 
            return self.parent_path_node.reds_in_path_counter( nodes, count + 1)
        else:
            if self.parent_path_node == None: # Root
                return count
            return self.parent_path_node.reds_in_path_counter( nodes, count)
    
    def __str__(self):
        if self.parent_path_node == None: # Root
            return self.node_id
        return self.node_id + " -- " + str(self.parent_path_node)

#many
def m(nodes, start_node_id, end_node_id, cardinality, total_edges):
    queue = [Path_node(start_node_id, None)]
    maxLength = -1
    while len(queue) > 0:
        path_node = queue.pop()
        for node_id in nodes[path_node.node_id].edges_out:
            if not path_node.in_path(node_id):
                new_path_node = Path_node(node_id, path_node)
                if node_id != end_node_id:
                    queue.append(new_path_node)
                else:
                    length = new_path_node.reds_in_path_counter(nodes, 0)
                    if length > maxLength:
                        maxLength = length
    if maxLength != -1:
        return maxLength
    else:
        return '-'
                


#none
def n(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass

#some
def s(nodes, start_node_id, end_node_id, cardinality, total_edges):
    pass


'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    #Arguments for Main
    ap.add_argument("-i", "--input", required=True,  help= "Input file containing graph")
    ap.add_argument("-n", "--none",  required=False, help="Run 'None' Algorithm", default=False, action = "store_true")
    ap.add_argument("-s", "--some",  required=False, help="Run 'Some' Algorithm", default=False, action = "store_true")
    ap.add_argument("-m", "--many",  required=False, help="Run 'Many' Algorithm", default=False, action = "store_true")
    ap.add_argument("-f", "--few",   required=False, help="Run 'Few' Algorithm",  default=False, action = "store_true")
    ap.add_argument("-a", "--any",   required=False, help="Run 'Any' Algorithm",  default=False, action = "store_true")
    ap.add_argument("-l", "--latex", required=False, help="Output as LateX",      default=False, action = "store_true")

    #Parse Arguments Given to Main
    args = vars(ap.parse_args())

    file_name = args["input"]
    nodes, start_node_id , end_node_id, cardinality, nodes_len, total_edges = parse_red_file(file_name)
    n_res, s_res, m_res, f_res, a_res = "?","?","?","?","?"

    if args["none"]:
        n_res = n(nodes, start_node_id , end_node_id, cardinality, total_edges)
    if args["some"]: 
        s_res = s(nodes, start_node_id , end_node_id, cardinality, total_edges)
    if args["many"]:
        m_res = m(nodes, start_node_id , end_node_id, cardinality, total_edges)
    if args["few"]:
        f_res = f(nodes, start_node_id , end_node_id, cardinality, total_edges)
    if args["any"]:
        a_res = a(nodes, start_node_id , end_node_id, cardinality, total_edges)

    output = output(args["input"], nodes_len, a_res, f_res, m_res, n_res, s_res, args["latex"])
    print(output)
'''END CODE'''
