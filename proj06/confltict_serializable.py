#I used a BFS algorithmic approach to find cycle in a graph using a Queue. I implemented all of this code by myself but used GeeksForGeeks as reference:
#https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs/
from itertools import combinations
def detect_conflict(action_a, action_b):
  if action_a.transaction == action_b.transaction:
    return True
  elif action_a.object_ != action_b.object_:
    return False
  elif action_a.is_write == False and action_b.is_write == False:
    return False
  else:
    return True

def determine_precedence(list_of_actions):
    precedence_list = []
    com = combinations(list_of_actions, 2)
    for pair in list(com):
        if detect_conflict(pair[0], pair[1]) == True:
            if pair[0].transaction != pair[1].transaction:
                precedence = (pair[0].transaction, pair[1].transaction)
                precedence_list.append(precedence)
    return sorted(list(set(precedence_list)))

def create_adjacency(list_of_tuples):
    adjacency_dict = {}
    for pair in list_of_tuples:
        if int(pair[1][1:]) not in adjacency_dict.keys():
            adjacency_dict[int(pair[1][1:])] = []
        if int(pair[0][1:]) not in adjacency_dict.keys():
            adjacency_dict[int(pair[0][1:])] = [int(pair[1][1:])]
        else:
            adjacency_dict[int(pair[0][1:])].append(int(pair[1][1:]))
    return adjacency_dict

def create_indegree_dict(dict_):
    indegree_dict = {}
    total_nodes = max(dict_.keys())
    for node in range(1,total_nodes+1):
        indegree_dict[node] = 0
    for key,value in dict_.items():
        for edge in value:
            indegree_dict[edge] += 1    
    return indegree_dict

def is_cyclic(dict_, indegree_dict):
    Q = []
    total_nodes = max(dict_.keys())
    visited_nodes = 0
    if  0 not in indegree_dict.values():
        return True
    else:
        for node,indegree in indegree_dict.items():
            if indegree == 0:
                Q.append(node)
        while(Q):
            removed_node = Q.pop()
            print(removed_node)
            visited_nodes += 1
            for neighbor in dict_[removed_node]:
                indegree_dict[neighbor] -= 1
                if indegree_dict[neighbor] == 0:
                    Q.append(neighbor)
       
        if visited_nodes != total_nodes:
            return True
        else:
            return False

def is_conflict_serializable(schedule):
    precedence_list = determine_precedence(schedule)
    adjacency_dict = create_adjacency(precedence_list)
    indegree_dict = create_indegree_dict(adjacency_dict)
    if not is_cyclic(adjacency_dict, indegree_dict):
        return True
    else:
        return False