from lark import Lark, Tree
import graphviz

# Load grammar from file
with open("grammar.lark", "r") as f:
    grammar_text = f.read()

# Create parsers for both LMD and RMD
parser_lmd = Lark(grammar_text, start='start', parser='lalr')  # LALR for LMD
parser_rmd = Lark(grammar_text, start='start', parser='earley')  # Earley for RMD

def parse_code(code, mode='both'):
    try:
        result = {}
        if mode in ['lmd', 'both']:
            tree_lmd = parser_lmd.parse(code)
            result['lmd'] = tree_lmd
        if mode in ['rmd', 'both']:
            tree_rmd = parser_rmd.parse(code)
            result['rmd'] = tree_rmd
        return result
    except Exception as e:
        return str(e)

def tree_to_graphviz(tree):
    dot = graphviz.Digraph(format='png')

    def add_nodes_edges(node, parent=None):
        node_id = str(id(node))
        if isinstance(node, Tree):
            label = node.data
        else:
            label = str(node)
        dot.node(node_id, label)
        if parent:
            dot.edge(parent, node_id)
        if isinstance(node, Tree):
            for child in node.children:
                add_nodes_edges(child, node_id)

    add_nodes_edges(tree)
    return dot

def _tree_to_string(tree):
    if isinstance(tree, Tree):
        return f"{tree.data} ({' '.join(_tree_to_string(child) for child in tree.children)})"
    return str(tree)

def get_lmd_steps(tree):
    if not isinstance(tree, Tree):
        return [str(tree)]
    
    steps = ["start"]
    current = tree
    while True:
        if isinstance(current, Tree):
            steps.append(_tree_to_string(current))
            if not current.children:
                break
            current = current.children[0]
        else:
            steps.append(str(current))
            break
    return steps

def get_rmd_steps(tree):
    if not isinstance(tree, Tree):
        return [str(tree)]
    
    steps = ["start"]
    current = tree
    while True:
        if isinstance(current, Tree):
            steps.append(_tree_to_string(current))
            if not current.children:
                break
            current = current.children[-1]
        else:
            steps.append(str(current))
            break
    return steps
