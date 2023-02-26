"""DFS (Deep First Search) Algorithm

DFS is a recursive algorithm that searches all of teh vertices on a graph or tree structure. It is also a transversal
algorithm, which will run across all nodes of the graph or tree.

The first approach of this algorithm is setting vertices on two categories:
    - Visited
    - Not Visited

The main purpose of the algorithm is marking every node as visited avoiding cycles.

DFS steps:
    - At start, put any of the vertices of the graph on top of the stack.
    - Take the top item of the stack and add it on the visited group.
    - Create a list of that vertex's adjacent nodes. Add the ones that aren't yet on the visited group on top of the stack.
    - Repeat steps 2 and 3 until the graph if finished.

Graphical example:

    0 ------3
    | \             |0| | | | | | VISITED
    |   2           |1|2|3|4| | | STACK
    | /   \
    1      4

Pseudo-code:

DFS(G,n)
    n.visited = True
    for each v @ G.adjacent[n]
        if v.visited == false
            DFS(G,v)

This algorithm complexity is equal to O(v) or O(n) since depends entirely on the graph size.
"""

def dfs(graph,start,visited=None):
    
    if visited is None:
        visited = set()

    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph,next,visited)
    
    return visited

graph = {
    '0': set(['1','2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

print(dfs(graph,'0'))