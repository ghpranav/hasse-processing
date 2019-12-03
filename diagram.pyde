from Link import Link
from Node import Node
import hasse
import input_data
from tinynumpy import tinynumpy as tnp

max_width = 1300
max_height = 700

def setup():
    size(1400, 800)


def draw():
    raw_data = input_data.get_data()
    
    set = []
    num = 0
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

    matrix = tnp.zeros(shape = (dim, dim), dtype = 'int32')
    for i in set:
        row = i[0] - 1
        col = i[1] - 1
        matrix[row, col] = 1

    print("Relation set R: ")
    print(set)
    
    print("Matrix: ")
    print(matrix)

    data = hasse.optimize_data(raw_data)
    quadrants = hasse.get_quadrants(data, max_height)
    nodes = hasse.add_nodes(data, quadrants, max_width)
    hasse.add_links(data, nodes)
    noLoop()


setup()
