class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.edge = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_edge(self, edg):
        self.edge.append(edg)


def print_tree(node, level):
    print(str(node.data) +" at level " +str(level))
    for x in range(0, len(node.children)):
        print_tree(node.children[x],level+1)
