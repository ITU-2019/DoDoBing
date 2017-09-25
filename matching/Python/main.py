'''Imports'''
import sys
from collections import deque

'''Fields'''
# g_men: { man_id => (man_name, [woman_id_1, ...]) }
g_men = {}

# g_women: { woman_id => (woman_name, { man_id => int_priority }) }
g_women = {}

# men_available: [man_id_1, ...]
men_available = []
'''fields End.'''

''' Parse file to internal data structure.
    @param: filename: The path of file to parse
'''
def parse_file(filename, men, women, unmatched_men):
    data = ""
    n = 0
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            if line[0] == 'n':
                n = int(line[2:])

            if line[0].isdigit():
                if line.find(":") != -1:
                    number = int(line[:line.find(":")])
                    string_line = line[line.find(" ")+1:line.find("\\n")].split(' ')
                    string_line_cleaned = [y for y in string_line if y != '']
                    priorities = ([int(i) for i in string_line_cleaned])
                    if number % 2 == 1:
                        unmatched_men.append(number)
                        men[number][1].extend(priorities)
                    else:
                        count = 0
                        for x in priorities:
                            women[number][1][x] = count
                            count += 1
                else:
                    number = int(line[0:line.find(" ")])
                    name = line[line.find(" ")+1:line.find("\\n")]
                    if number % 2 == 1:
                        men[number] = (name, deque())
                    else:
                        women[number] = (name, {})

    # Reverse list to make sure we look at men in the read order.
    unmatched_men.reverse()
    
'''The passing file code. END'''

''' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Helper functions
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

''' Function that prints out a matching to stdout.
    @param: our_matching: The final stable matching pairs
    @param: men: The dictionary of men
    @param: women: The dictionary of women
'''
def output_matching(out_matching, men, women):
    for man in men:
        for w,m in out_matching.items():
            if man == m:
                print(men[m][0], "--", women[w][0])

''' Returns the next unmatched man's id from the stack of unstacked men.
    @param: umatched_men: The Stack of unmatched men
'''
def get_next_unmatched_man_id(unmatched_men):
    if not unmatched_men:
        return None
    else:
        return unmatched_men.pop()

''' Returns The next woman in a specific man's stack of women.
    @param: man_id: The id of the man
    @param: men: The dictionary of men
'''
def get_highest_woman_id(man_id, men):
    if not men[man_id][1]:
        return None

    return men[man_id][1].popleft()

''' Adds a matching to the dictionary of matchings.
    @param: matchings: The dictionary of matchings
    @param: man_id: The id of the man
    @param: woman_id: The id of the woman
'''
def add_matching(matchings, man_id, woman_id):
    matchings[woman_id] = man_id

''' Returns true if the man and the woman is a preffered match compared to the current match otherwise return false.
    @param: matchings: The dictionary of current matchings
    @param: man_id: The id of the man
    @param: woman_id: The id of the woman
'''
def is_preferred_match(matchings, man_id, woman_id):
    cur_man_id = matchings[woman_id]
    if (g_women[woman_id][1][man_id] < g_women[woman_id][1][cur_man_id]):
        return True
    else:
        return False

''' Replace a matcing in the matchings dictionary with the (man_id, woman_id).
    @param: matchings: The dictionary of current matchings
    @param: man_id: The id of the man
    @param: woman_id: the id of the woman
'''
def replace_matching(matchings, man_id, woman_id):
    cur_man_id = matchings[woman_id]
    matchings[woman_id] = man_id
    men_available.append(cur_man_id)

''' Adds the man to the unmatched stack again.
    @param: unmatched_men: The unmatched stack
    @param: man_id: The id of the man.
'''
def reject_man(unmatched_men, man_id):
    unmatched_men.append(man_id)

''' Return true if woman is already matched otherwise return false.
    @param: woman_id: The id of the woman to check
    @param: matchings: The dictionary of current matchings
'''
def is_woman_matched(woman_id, matchings):
    if woman_id in matchings:
        return True
    else:
        return False

''' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Helper Functions End
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''


'''Algorithm '''
def gs_algorithm(men, women, men_available):
    #Initialize M to empty matching.
    m = {}

    while men_available: # Check if we have more men to match
        man_id = get_next_unmatched_man_id(men_available)
        if man_id is None:
            break # All men are matched

        woman_id = get_highest_woman_id(man_id, men)
        if not is_woman_matched(woman_id, m): # Check if woman is already matched
            add_matching(m, man_id, woman_id)
        elif is_preferred_match(m, man_id, woman_id): # Check if this man is a preffered match
            replace_matching(m, man_id, woman_id)
        else:
            reject_man(men_available, man_id) # Put the man back on unmatched list
    return m
'''Algorithm End'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        parse_file(args[1], g_men, g_women, men_available)
    output_matching(gs_algorithm(g_men, g_women, men_available), g_men, g_women)
'''END CODE'''
