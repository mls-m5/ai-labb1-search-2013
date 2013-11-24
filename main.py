
from ailabb1 import *
import gui
from search import *

graph = None

def findPath():
	graph = Graph.lastGraph
	gui.apGui.apwindow.clear()
	graph.draw()
	path, explored = depthFirstSearch(graph,"Tybble", "Solhaga")
	graph.drawPath(path)
	gui.apGui.apwindow.drawText(500, 20, str(explored))

def findAPath():
	graph = Graph.lastGraph
	gui.apGui.apwindow.clear()
	graph.draw()
	path, explored = asearch(graph, "Tybble", "Solhaga")
	graph.drawPath(path)
	gui.apGui.apwindow.drawText(500, 20, str(explored))


def main():

	global graph
		
	frame = Frame(gui.apGui.apwindow)
	frame.place(x=0, y=0)
	button = Button(frame, text="hej", anchor=W, command=findPath)
	button.pack()
		
	button2 = Button(frame, text="hej2", command=findAPath)
	button2.pack()
		
	graph = Graph()
	graph.loadFile()
	graph.draw()
		
	gui.apGui.apwindow.start()


if __name__ == "__main__":
	main()
