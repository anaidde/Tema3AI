#!/usr/bin/python3.8

import re


def arc_consistency(input_file_name):
    nodes_data = {}
    
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            split_data = line.split(':')
            node = split_data[0]
            
            split_data = split_data[1].split(';')
            neighbours_list = re.sub("[{|}|\\s]", "", split_data[0]).split(",")
            colors_set = set(re.sub("[{|}|\\s]", "", split_data[1]).split(","))
            
            nodes_data[node] = { "neighbours": neighbours_list, "colors": colors_set }
            
    edges_queue = []
    for node, node_data in nodes_data.items():
        for neighbour in node_data["neighbours"]:
            edges_queue.append((node, neighbour))
    
    while len(edges_queue) > 0:
        edge = edges_queue.pop(0)
        node1_name = edge[0]
        node2_name = edge[1]
        node1_data = nodes_data[node1_name]
        node2_data = nodes_data[node2_name]
        
        if len(node2_data["colors"]) == 1:
            color = next(iter(node2_data["colors"]))
            
            if color in node1_data["colors"]:
                node1_data["colors"].remove(color)
                
                for neighbour in node1_data["neighbours"]:
                    edges_queue.append((neighbour, node1_name))
                
    nodes_coloring = {}
    for node, node_data in nodes_data.items():
        if len(node_data["colors"]) != 1:
            return None
        nodes_coloring[node] = next(iter(node_data["colors"]))
        
    return nodes_coloring
    

if __name__ == "__main__":
    print(arc_consistency("test1.txt"))
    print(arc_consistency("test2.txt"))
    
