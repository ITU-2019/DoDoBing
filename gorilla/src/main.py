'''Imports'''

'''Imports end'''
'''Fields'''

'''Fields end'''

'''Parse'''

def parse_dna_file(filename):
    pass

def parse_penalty_file(filename):
    pass

'''Parse end'''


'''Helper methods'''

def output(result):
    pass

'''Helper methods end'''

'''Algorithm'''
def space_efficient_alignment():
    

def backward_space_efficient_alignment():
    pass

def devide_and_conquer_alignment(dna_1, dna_2):
    # let m be the number of ymbols in dna_1
    # let n be the number of symbols in dna_2
    # if m <= 2 or n <= then 
        # compute optimal alignment using Allignemnt(X,Y)
    # call Space-Efficient-Alignment (X,Y[1:n/2])
    # Call Backward_Space_efficient_alignment(X,Y[n/2 +1:n])
    
    # Let q be the index minimizing f(q, n/2)+ g(q, n/2)
    # add (q,n/2) to global list P

    # devide_and_conquer_alignment(dna_1[1:q], dna_2[1:n/2])
    # devide_and_conquer_alignment(dna_1[q + 1:n], dna_2[n/2 +1:n])
    # return P....

def main_algo(all_dna, all_penalty):
    for i in range(len(all_dna)):
        for j in range (i, len(all_dna)):
            if i != j:
                res = devide_and_conquer_alignment(all_dna[i], all_dna[j], all_penalty)
                output(res)
'''Algorithm'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        all_dna = parse_dna_file(args[1])
        all_penalty = parse_penalty_file(args[2])
        main_algo(all_dna, all_penalty)
        
'''END CODE'''

