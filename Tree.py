class TreeNode():
    def __init__(self,value,w):
        self.data = value
        self.weight = w
        self.left = None
        self.right = None
        

char = {'a' : 10, 'l' : 11, 'b' : 5, '1' : 4, ' ' : 8, '/' : 12, 'k' : 15}


class Tree():
    @staticmethod
    def genNodes(nodeDict):
        m = []
        for i in nodeDict:
           m.append(TreeNode(i,nodeDict[i]))
        m.sort(key = lambda x: x.weight)
        return m

    @staticmethod
    def genTree(nodeList):    
        if(len(nodeList) == 1):
           return nodeList[0]
        node = TreeNode("",nodeList[0].weight + nodeList[1].weight)
        node.left = nodeList[0]
        node.right = nodeList[1]
        
        del nodeList[1]
        del nodeList[0]

        nodeList.append(node)
        nodeList.sort(key = lambda x: x.weight)

        return Tree.genTree(nodeList)
    
    @staticmethod
    def Traverse(tree):
        if tree:
            Tree.Traverse(tree.left)
            print ("Tree Weight: "),
            print (tree.weight )
            print ("Tree Data: "),
            print (tree.data)
            Tree.Traverse(tree.right)

    
    @staticmethod
    def PathInverse(tree, binstr):
        if(binstr == ""):
            return tree.data
        if(binstr[0] == '0'):
            if(tree.left):
                return Tree.PathInverse(tree.left,binstr[1:])
            else:
                return tree.data
        if(binstr[0] == '1'):
            if(tree.right):
                return Tree.PathInverse(tree.right, binstr[1:])
            else:
                return tree.data


    
    @staticmethod
    def Paths(tree,path,paths):
        if(tree.left):
            path += str(0)
            Tree.Paths(tree.left,path,paths)
        if(tree.data != ""):
            paths[tree.data] = path
        path = path[0:-1]
        if(tree.right):
            path += str(1)
            Tree.Paths(tree.right,path,paths)
        


if __name__ == '__main__':
    tree = Tree.genTree(Tree.genNodes(char))
    paths = {}
    Tree.Paths(tree,"",paths)
    print (paths)

#    Tree.Traverse(tree)
    print (Tree.PathInverse(tree,"1"))
