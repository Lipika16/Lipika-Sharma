#Function for storing matrix into the dictionary 
def dist_matrix(filename):
    #empty dictionary for storing the result
    matrix_dict = {}
    counter = 0
    with open(filename, 'r') as f:
        keys = f.readline().split()
        # this will give us list of keys
        #Reading into the file
        for line in f:
            line = line.split()
            #print(line)
            #temporary dictionary for storing
            temp_dict = {}
            #looping in length of keys
            for i in range(len(keys)):
                #putting keys with dictionary of its values
                temp_dict[keys[i]] = float(line[i + 1])
                #print(temp_dict)
            matrix_dict[keys[counter]] = temp_dict
            counter += 1
    return matrix_dict

print(dist_matrix("small-distances.txt"))


def nested_tuple(obj):
    if isinstance(obj, tuple):
        if isinstance(obj[0], tuple) and not isinstance(obj[1], tuple):
            return 1 + nested_tuple(obj[0])
        elif isinstance(obj[1], tuple) and not isinstance(obj[0], tuple):
            return 1 + nested_tuple(obj[1])
        elif isinstance(obj[1], tuple) and isinstance(obj[0], tuple):
            return nested_tuple(obj[0]) + nested_tuple(obj[1])
        else:
            return 2
    elif isinstance(obj, str):
        return 1
    
#print(nested_tuple(((('A','B'),'C'),('D','E'))))

# Merge two clusters
def merge_clust(dist_mat, clust1, clust2):
    # Getting the number of elements in each cluster
    clust_1 = nested_tuple(clust1)
    clust_2 = nested_tuple(clust2)
    # Updating distance matrix
    temp_dict = {}
    for k, v in dist_mat.items():
        if k not in (clust1, clust2):
            #formula from handout to calculate distance
            new_dist = ((clust_1 * dist_mat[k][clust1]) + (clust_2 * dist_mat[k][clust2])) / (
                clust_1 + clust_2)
            dist_mat[k][(clust1, clust2)] = new_dist
            temp_dict[k] = new_dist
    dist_mat[(clust1, clust2)] = temp_dict
    dist_mat[(clust1, clust2)][(clust1, clust2)] = 0.0
    # Clean distance matrix
    del dist_mat[clust1]
    del dist_mat[clust2]
    for k, v in dist_mat.items():
        if k != (clust1, clust2):
            del v[clust1]
            del v[clust2]
            
dist_mat = dist_matrix("small-distances.txt")