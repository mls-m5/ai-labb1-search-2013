
from node import *
import gui

class Link:
	Id = 0
	Node1 = Node("0;apa;0;0")
	Node2 = Node("0;apa;0;0")
	 
	def __init__(self, content, graph):
		splitz = str(content).split(";") 
		self.Id = splitz[0]
		self.Node1 = graph.getNode(int(splitz[1]))
		self.Node2 = graph.getNode(int(splitz[2]))

		
	def draw(self, width):
		gui.apGui.apwindow.drawLine(self.Node1.X, self.Node1.Y, self.Node2.X, self.Node2.Y, width)
	
if __name__ == "__main__":
	from main import *
	main()
	
