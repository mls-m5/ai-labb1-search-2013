
from node import *
from link import *
import gui

class Graph:
	nodes = []
	links = []
	 
	def checkReachable(self, node1, node2):
		frontier = 1
		
		
	def selectBest(self, frontier):
		#different for different types of searches
		return next(frontier.itervalues())
	
	def calculateScore(self, path):
		pass
	

	def __init__(self):
		self.nodes = []
		self.links = []
		Graph.lastGraph = self
	
	def getNode (self, name):
		for n in self.nodes:
			if (n.Id == name):
				return n
			if (n.Name == name):
				return n
		return "ingenteng"

	def getAllLinkFrom(self, node):
		allLinks = []
		for l in self.links:
			if l.Node1 == node:
				allLinks.append(l.Node2)
			if l.Node2 == node:
				allLinks.append(l.Node1)
		return allLinks
		
	def getLocations(self, Id):
		for l in links:
			if (l.Id == Id):
				return l
	
	def draw(self):
		gui.apGui.apwindow.clear()
		for l in self.links:
			l.draw(1)
		for n in self.nodes:
			n.draw()
		
		#for n in self.nodes:
		#	n.drawNet(self)
	
	def resetNodeData(self):
		for n in self.nodes:
			n.parent = None			
			n.Score = 0
			n.Explored = False
	
	def drawPath(self, path):
		if len(path) < 2: 
			return
		p = path[0]
		for n in path[1:]:
			gui.apGui.apwindow.drawLine(n.X, n.Y, p.X, p.Y, 4)
			p = n
	
	def loadFile(self):
		for line in open("locations.csv"):
			self.nodes.append(Node(line))
			
		for line in open("links.csv"):
			self.links.append(Link(line, self))
	
	def printPath(self, path):
		printstr = "Path: "
		for n in path:
			printstr = printstr + "->" + n.Name
			
		print(printstr)
	

if __name__ == "__main__":
	from main import *
	main()
