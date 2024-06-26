"""
    Algoritmo per l'ordinamento topologico in un DAG
"""

from typing import Dict, List

def dfs(g: Dict[str, List[str]], v: str) -> List[str]:
    
    stack = []
    visited = set()
    stack.append(v)
    result = []

    while len(stack):

        current = stack.pop()
        result.append(current)

        if current not in visited:
            visited.add(current)

            for neighbor in g[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return result;
    


def ordinamento_topologico(g: Dict[str, List[str]]) -> List[str]:
    
    stack = []
    visited = set()

    for vertex in g:
        if vertex not in visited:
            dfs(g, vertex)

    top_order = []

    while stack:
        top_order.append(stack.pop())

    return top_order


if __name__ == "__main__":
    
    graph = {
        'A': ['B'],
        'B': ['D', 'E'],
        'C': ['A', 'B', 'F'],
        'D': ['E'],
        'E': ['F'],
        'G': ['C', 'F'],
        'F': []
    }    

    print(dfs(graph, 'A'))
    print(ordinamento_topologico(graph))
