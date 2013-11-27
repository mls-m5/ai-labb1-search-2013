from math import sqrt


def recreatePath(node):
    #print("recreating path")
    if node.parent is None:
        return [node]
    else:
        n = node.parent
        path = [n, node]
        while n.parent != n:
            n = n.parent
            path.insert(0, n)
    return path


def depthFirstSearch(graph, start, target):
    graph.resetNodeData()
    startNode = graph.getNode(start)
    targetNode = graph.getNode(target)
    startNode.parent = startNode #To make the recreation of path stop
    startNode.Explored = -1
    frontier = [startNode]
    explored = 0
    while 1:
        if not len(frontier):
            return None
        node = frontier.pop()

        for next in graph.getAllLinkFrom(node):
            if not next.Explored: # ie. not explored
                explored += 1
                next.Explored = explored
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
        #return die
    #return NodeDistance(node, targetNode)
    return distance + NodeDistance(path[-1], targetNode)


def asearch(graph, start, target):
    graph.resetNodeData()
    startNode = graph.getNode(start)
    targetNode = graph.getNode(target)
    startNode.parent = startNode #To make the recreation of path stop
    startNode.Explored = -1
    frontier = [startNode]
    explored = 0
    while 1:
        if not len(frontier):
            return None
        node = frontier.pop()

        connectedNodes = graph.getAllLinkFrom(node)

        for next in connectedNodes:
            if next.parent is None:
                next.parent = node
            score = next.Score = evaluatePath(next, targetNode)
            if next.Score == 0:
                next.Score = score
            else:
                if score < next.Score:
                    next.Score = score
                    next.Explored = 0

        sortedNodes = sorted(connectedNodes, key=lambda n: - n.Score)
        #sortedNodes = connectedNodes[::-1]
        for next in sortedNodes:
            if not next.Explored: # ie. not explored
                explored += 1
                next.Explored = explored
                explored
                if next == targetNode:
                    return recreatePath(next), explored
                frontier.append(next)


if __name__ == "__main__":
    from main import *

    main()
