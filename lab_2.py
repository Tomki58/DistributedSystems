graph = {'0': {'in': ['1'], 'out': ['2']}, '1': {'in': ['3'], 'out': ['0', '2']},
        '2': {'in': ['0', '1'], 'out': ['4']}, '3': {'in': ['4'], 'out': ['1']},
        '4': {'in': ['2'], 'out': ['3']}}


class Node:

    def __init__(self, ID):
        self.ID = ID
        self.out = set()
        self.inc = {self.ID}
        self.ninc = set()
        self.inp = dict()

def parse_graph(graph : dict):
    nodes = []
    for nodeID in graph.keys():
        tmpNode = Node(nodeID)
        tmpNode.out = set(graph[nodeID]['out'])
        tmpNode.inp = {k: False for k in graph[nodeID]['in']}
        nodes.append(tmpNode)

def find_in_list(nodes, nodeID):
    return next((node for node in nodes if node.ID == nodeID), None)

def flinn_algorithm(nodes, iniNodeID):

    iniNode = find_in_list(nodes, iniNodeID)
    activeNodes = [iniNode]
    # while iniNodeID.inc != iniNodeID.ninc:
    for node in activeNodes:
        outNodes = [find_in_list(nodes, nodeID) for nodeID in node.out]
        
        pass
    pass

if __name__ == "__main__":
    
    parse_graph(graph)