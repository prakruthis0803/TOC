# -*- coding: utf-8 -*-
from lark import Lark, Tree
import graphviz

# Load grammar from file
with open("grammar.lark", "r") as f:
    grammar_text = f.read()

# Create parsers for both LMD and RMD
parser_lmd = Lark(grammar_text, start='start', parser='lalr')  # LALR for LMD
parser_rmd = Lark(grammar_text, start='start', parser='earley')  # Earley for RMD

def parse_code(code, mode='both'):
    """Parse the input code and return parse trees"""
    try:
        # Clean up input
        code = code.strip()
        result = {}

        # Generate LMD parse tree
        if mode in ['lmd', 'both']:
            try:
                tree_lmd = parser_lmd.parse(code)
                if isinstance(tree_lmd, Tree):
                    # Convert operator tokens to appropriate node types
                    result['lmd'] = preprocess_tree(tree_lmd)
                else:
                    raise ValueError("Invalid parse tree structure for LMD")
            except Exception as e:
                raise ValueError(f"LMD parsing error: {str(e)}")

        # Generate RMD parse tree
        if mode in ['rmd', 'both']:
            try:
                tree_rmd = parser_rmd.parse(code)
                if isinstance(tree_rmd, Tree):
                    # Convert operator tokens to appropriate node types
                    result['rmd'] = preprocess_tree(tree_rmd)
                else:
                    raise ValueError("Invalid parse tree structure for RMD")
            except Exception as e:
                raise ValueError(f"RMD parsing error: {str(e)}")

        return result
    except Exception as e:
        return str(e)

def preprocess_tree(tree):
    """Process the parse tree to ensure proper node types"""
    if not isinstance(tree, Tree):
        return tree
        
    # Process children first
    new_children = [preprocess_tree(child) for child in tree.children]
    
    # Handle specific node types
    if tree.data == 'add':
        # Ensure we have exactly two operands for addition
        if len(new_children) != 2:
            new_children = [new_children[0], Tree('number', [new_children[-1]])]
    elif tree.data == 'mul':
        # Ensure we have exactly two operands for multiplication
        if len(new_children) != 2:
            new_children = [new_children[0], Tree('number', [new_children[-1]])]
            
    # Create new tree with processed children
    return Tree(tree.data, new_children)

def tree_to_graphviz(tree):
    dot = graphviz.Digraph(format='png')
    
    def clean_label(label):
        """Clean the label for display"""
        label = str(label)
        if label in ['+', '*', '(', ')']:
            return f'"{label}"'
        return label

    def add_nodes_edges(node, parent=None):
        node_id = str(id(node))
        if isinstance(node, Tree):
            label = node.data
            if label == 'start':
                label = 'ROOT'
            elif label == 'add':
                label = '+'
            elif label == 'mul':
                label = '*'
        else:
            label = clean_label(node)
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
