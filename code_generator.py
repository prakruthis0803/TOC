from lark import Tree

class CodeGenerator:
    @staticmethod
    def generate_python(tree):
        if not isinstance(tree, Tree):
            return str(tree)
        
        if tree.data == 'add':
            left = CodeGenerator.generate_python(tree.children[0])
            right = CodeGenerator.generate_python(tree.children[1])
            return f"({left} + {right})"
        
        elif tree.data == 'mul':
            left = CodeGenerator.generate_python(tree.children[0])
            right = CodeGenerator.generate_python(tree.children[1])
            return f"({left} * {right})"
        
        return str(tree)

    @staticmethod
    def generate_javascript(tree):
        if not isinstance(tree, Tree):
            return str(tree)
        
        if tree.data == 'add':
            left = CodeGenerator.generate_javascript(tree.children[0])
            right = CodeGenerator.generate_javascript(tree.children[1])
            return f"({left} + {right})"
        
        elif tree.data == 'mul':
            left = CodeGenerator.generate_javascript(tree.children[0])
            right = CodeGenerator.generate_javascript(tree.children[1])
            return f"({left} * {right})"
        
        return str(tree)

    @staticmethod
    def generate_cpp(tree):
        if not isinstance(tree, Tree):
            return str(tree)
        
        if tree.data == 'add':
            left = CodeGenerator.generate_cpp(tree.children[0])
            right = CodeGenerator.generate_cpp(tree.children[1])
            return f"({left} + {right})"
        
        elif tree.data == 'mul':
            left = CodeGenerator.generate_cpp(tree.children[0])
            right = CodeGenerator.generate_cpp(tree.children[1])
            return f"({left} * {right})"
        
        return str(tree)
