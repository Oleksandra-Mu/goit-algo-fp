import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex

class Node:
    def __init__(self, key, color="#37fad9"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

def color_pallete(min_value, max_value, value):
    value_ratio = (value - min_value) / (max_value - min_value)
    return value_ratio * 255

def colors_dfs(node, color_map, depth=0, max_depth=5):
    if node:
        color_intensity = color_pallete(0, max_depth, depth)
        node.color = to_hex([color_intensity / 255, 0, color_intensity / 255 * 0.6])  # Встановлюємо колір вузла
        color_map[node.id] = node.color
        colors_dfs(node.left, color_map, depth + 1)
        colors_dfs(node.right, color_map, depth + 1)

def colors_bfs(root, max_depth=5):
    color_map = {}
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node:
            color_intensity = color_pallete(0, max_depth, depth)
            node.color = to_hex([color_intensity / 255, 0, color_intensity / 255 * 0.6])
            color_map[node.id] = node.color
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return color_map

def draw_tree(tree_root, type=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if type == 'DFS':
        color_map = {}
        colors_dfs(tree_root, color_map)
    else:
        color_map = colors_bfs(tree_root)

    colors = [color_map.get(node) for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors,font_color='white')
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root, type='BFS')
draw_tree(root, type='DFS')
