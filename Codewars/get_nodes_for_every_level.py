def get_nodes_level(tree):
    def helper(acc, node, level):
        if node is None:
            return acc

        if (len(acc) < level):
            acc.append([])

        acc[level].append(node)

        helper(acc, node.left, level+1)
        helper(acc, node.right, level+1)

    result = []
    helper([], tree, 0)
    return result
