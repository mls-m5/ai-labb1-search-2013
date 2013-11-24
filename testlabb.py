import unittest
from ailabb1 import *
import search

class labbtest (unittest.TestCase):
# 	graph = Graph()
# 	def setUp(self):
# 		self.graph.loadFile()


	def getTestGraph1(self):
		graph = Graph()
		graph.nodes.append(Node("1;sverige;-1;10"))
		graph.nodes.append(Node("2;usa;1;20"))
		graph.links.append(Link("1;1;2", graph))
		return graph

	def testConnection(self):
		graph = self.getTestGraph1()
		self.assertEqual(len(graph.nodes), 2)
		
	def testLinks(self):
		graph = self.getTestGraph1()
		print(len(graph.links))
		self.assertEqual(len(graph.links), 1, "Antalet kopplingar")
		self.assertNotEqual(graph.links[0].Node1, None, "Tom nod")
		self.assertNotEqual(graph.links[0].Node2, None, "Tom nod")
		
		
	def testLoadFromFile(self):
		graph = Graph()
		graph.loadFile()
		#graph.asearch("Norr", "Varberga")
		path, explored = search.depthFirstSearch(graph, "Norr", "Varberga")
		
		Graph.printPath(graph, path)
		


def main():
	print("hej")
	unittest.main()

if __name__ == '__main__':
    main()



