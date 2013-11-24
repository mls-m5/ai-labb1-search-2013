
import ailabb1
from math import sqrt

def recreatePath(node):
	print("recreating path")
	if node.parent == None:
		return [node]
	else:
		n = node.parent
		path = [node, n]
		while n.parent != n:
			n = n.parent
			path.insert(0,n)
	return path

def depthFirstSearch(graph, start, target):
	graph.resetNodeData()
	startNode = graph.getNode(start)
	targetNode = graph.getNode(target)
	startNode.parent = startNode #To make the recreation of path stop
	frontier = [startNode]
	explored = 0
	while 1:
		if not len(frontier):
			return None
		node = frontier.pop()
		
		for next in graph.getAllLinkFrom(node):
			if next.Explored == False: # ie. not explored
				next.Explored = True
				explored = explored + 1
				next.parent = node
				if next == targetNode:
					return recreatePath(next), explored
				frontier.append(next)
				#frontier.insert(0,next)
				

def NodeDistance(node1, node2):
	return sqrt((node2.X - node1.X) ** 2 + (node2.Y - node1.Y) ** 2)

def evaluatePath(node, targetNode):
	distance = 0
	path = recreatePath(node)
	if len(path) < 2:
		return 0
	for node in path[1:]:
		distance += NodeDistance(node, node.parent)
	return distance + NodeDistance(path[-1], targetNode)

def asearch(graph, start, target):
	graph.resetNodeData()
	startNode = graph.getNode(start)
	targetNode = graph.getNode(target)
	startNode.parent = startNode #To make the recreation of path stop
	frontier = [startNode]
	explored = 0
	while 1:
		if not len(frontier):
			return None
		node = frontier.pop()
		
		connectedNodes = graph.getAllLinkFrom(node)
		
		for next in connectedNodes:
			if next.parent == None:
				next.parent = node
			if next.Score == 0:
				next.Score = evaluatePath(node, targetNode)
		
		sortedNodes = sorted(connectedNodes, key=lambda node: node.Score)
		for next in sortedNodes:
			if next.Explored == False: # ie. not explored
				explored += 1
				next.Explored = True
				explored
				if next == targetNode:
					return recreatePath(next), explored
				frontier.append(next)
				#frontier.insert(0,next)



if __name__ == "__main__":
	from main import *
	main()
