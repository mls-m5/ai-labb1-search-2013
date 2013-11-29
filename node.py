import gui

class Node:
    Id = 0
    X = 0
    Y = 0
    Name = ""
    Score = 0
    Explored = 0

    def __init__(self, initStr):
        splitz = str(initStr).split(";");
        self.Id = int(splitz[0])
        self.Name = splitz[1]
        self.X = float(splitz[2])
        self.Y = float(splitz[3])
        self.parent = None
        self.Score = 0

    def draw(self):
        gui.apGui.apwindow.drawText(self.X, self.Y, text=self.Name)
        if self.Score > 0:
            gui.apGui.apwindow.drawText(self.X, self.Y - 20, text=round(self.Score, 2))
        if self.Explored > 0:
            gui.apGui.apwindow.drawText(self.X, self.Y + 20, text=self.Explored)

    def drawNet(self, graph):
        apAll = graph.getAllLinkFrom(self)
        for n in apAll:
            gui.apGui.apwindow.drawLine(self.X, self.Y, n.X, n.Y, 2)


if __name__ == '__main__':
    from main import *

    main()
