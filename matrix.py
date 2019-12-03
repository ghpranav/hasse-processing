from tinynumpy import tinynumpy as np

set = []
num = 0
dim = 0


def get_set(raw_data):
    dim = 0
    for data in raw_data:
        for item in data:
            if(isinstance(item, int)):
                num = item
                dim += 1
                set.append([num, num])
            if(isinstance(item, list)):
                for ele in item:
                    set.append([num, ele])

    return set


def get_matrix(set):
    print(dim)
    matrix = np.zeros(dim, dim)

    for i in set:
        row = i[0]
        col = i[1]

        matrix[row][col] = 1

    return matrix
