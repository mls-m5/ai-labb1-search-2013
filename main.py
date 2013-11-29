from ailabb1 import *
import gui
from search import *

fromPath = StringVar()
fromPath.set("Tybble")
toPath = StringVar()
toPath.set("Solhaga")


def findPath():
    graph = Graph.lastGraph
    gui.apGui.apwindow.clear()
    path, explored = depthFirstSearch(graph, fromPath.get(), toPath.get())
    graph.draw()
    graph.drawPath(path)
    gui.apGui.apwindow.drawText(500, 20, str(explored))


def findAPath():
    graph = Graph.lastGraph
    gui.apGui.apwindow.clear()
    path, explored = asearch(graph, fromPath.get(), toPath.get())
    graph.draw()
    graph.drawPath(path)
    gui.apGui.apwindow.drawText(500, 20, str(explored))


def main():
    global graph, fromPath, toPath

    frame = Frame(gui.apGui.apwindow)
    frame.place(x=0, y=0)
    button = Button(frame, text="Depth/bredth-first", anchor=W, command=findPath)
    button.pack()

    button2 = Button(frame, text="A*search", command=findAPath)
    button2.pack()

    fromEntry = Entry(frame, textvariable=fromPath)

    fromEntry.pack()
    toEntry = Entry(frame, textvariable=toPath)
    toEntry.pack()

    graph = Graph()
    graph.loadFile()
    graph.draw()

    gui.apGui.apwindow.start()


if __name__ == "__main__":
    main()
