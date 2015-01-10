# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    #dfs
    def cloneGraph(self, node):

        def dfs(input, map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for i in input.neighbors:
                output.neighbors.append(dfs(i,map))
            
            return output

        
        if node == None:
            return None
        dict = {}
        return dfs(node,dict)
    #bfs
    def cloneGraph1(self,node):
        if node == None:
            return None
        q = [node]
        dict={}
        nodeCloned = UndirectedGraphNode(node.label)
        dict[node] = nodeCloned
        while q:
            q1 = []
            while q:
                tmp = q.pop(0)
                for i in tmp.neighbors:
                    if i in dict:
                        dict[tmp].neighbors.append(dict[i]) 
                    else:
                        temp = UndirectedGraphNode(i.label)
                        dict[i] = temp
                        dict[tmp].neighbors.append(temp)
                        q1.append(i)          
            q = q1
        return nodeCloned
                    
        
        
