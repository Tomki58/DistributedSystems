graph = {	'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['G', 'H'],
			'D': ['B', 'E'], 'E': ['B', 'D'], 'F': ['B', 'G'],
			'G': ['F', 'C'], 'H': ['C']	
		}


# graph = { 'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B'], 'D': ['B']}

# graph = 

class Graph:

	def __init__(self, graphDict : dict):
		self.nodes = [Node(name) for name in graphDict.keys()]
		for node in self.nodes:
			node.out = self.find_by_ID_v2(*graphDict[node.ID])

	def find_by_ID_v2(self, *args):
		if len(args) != 0:
			nodesList = []
			for name in args:
				nodesList.append(next(x for x in self.nodes if x.ID == name))
			return nodesList

	def card(self, nodeId):
		node = self.find_by_ID_v2(nodeId)[0]
		return len(node.out)

	def recieve_token(self, node, preNode):
		node.pre = preNode if node.pre is None else node.pre
		node.counter += 1
		# for neigh in [outNode for outNode in node.out if outNode != node.pre]:
		# 	self.recieve_token(neigh, node)
		
		if node.counter == self.card(node.ID):
			if node.pre is None:
				print('return Ok')
				pass
			else:
				self.recieve_token(node.pre, None)

	def send_token(self, node):
		for neigh in [newNode for newNode in node.out if newNode != node.pre]:
			self.recieve_token(neigh, node)

	def echo_algorithm(self, iniNodeId : str):
		iniNode = self.find_by_ID_v2(iniNodeId)[0]
		nodeQueue = [iniNode]
		for node in nodeQueue:
			if iniNode.counter != self.card(iniNode.ID):
				self.send_token(node)
				nodeQueue.extend([neigh for neigh in node.out if neigh != node.pre])
			else:
				break
	

class Node:

	def __init__(self, ID):
		self.ID = ID
		self.out = []
		self.counter = 0
		self.pre = None

	def __repr__(self):
		resStr = "%s: " % self.ID + "rec = %d" % self.counter
		return resStr

def parse_graph(graph : dict):
	nodeList = list()
	for ID, _ in graph.items():
		nodeList.append(Node(ID))
	return nodeList


if __name__ == "__main__":
	# echo_algorithm(graph, 0)
	fooGraph = Graph(graph)
	# for item in fooGraph.nodes:
	# 	print(item)
	fooGraph.echo_algorithm('A')
	for node in fooGraph.nodes:
		print(node)