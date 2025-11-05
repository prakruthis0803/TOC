from lark import Tree

class ExpressionEvaluator:
    def __init__(self):
        self.variables = {}
        
    def clear(self):
        """Clear all stored variables"""
        self.variables.clear()

    def set_variable(self, name, value):
        """Set a variable value for evaluation"""
        self.variables[name] = value

    def evaluate(self, tree):
        """Evaluate the parsed expression tree"""
        if not isinstance(tree, Tree):
            value = str(tree).strip()
            try:
                return float(value)
            except ValueError:
                if value in self.variables:
                    return float(self.variables[value])
                raise ValueError(f"Variable '{value}' not defined")

        if tree.data == 'start':
            return self.evaluate(tree.children[0])
        
        elif tree.data == 'single':
            return self.evaluate(tree.children[0])
            
        elif tree.data == 'single_factor':
            return self.evaluate(tree.children[0])
            
        elif tree.data == 'add':
            # Addition: evaluate both operands and add
            left = float(self.evaluate(tree.children[0]))
            right = float(self.evaluate(tree.children[1]))
            return left + right
            
        elif tree.data == 'mul':
            # Multiplication: evaluate both operands and multiply
            left = float(self.evaluate(tree.children[0]))
            right = float(self.evaluate(tree.children[1]))
            return left * right
            
        elif tree.data == 'number':
            # Convert number token to float
            return float(tree.children[0])
            
        elif tree.data == 'var':
            # Look up variable value
            var_name = str(tree.children[0])
            if var_name in self.variables:
                return float(self.variables[var_name])
            raise ValueError(f"Variable '{var_name}' not defined")
            
        elif tree.data == 'paren':
            # Handle parenthesized expressions
            return self.evaluate(tree.children[0])
            
        elif tree.data in ['expr', 'term', 'factor']:
            # Pass through these nodes
            return self.evaluate(tree.children[0])
            
        else:
            raise ValueError(f"Unknown operation: {tree.data}")

    def validate_tree(self, tree):
        """Validate that all variables in the tree are defined"""
        undefined_vars = set()
        
        def check_vars(node):
            if isinstance(node, Tree):
                if node.data == 'var':
                    var_name = str(node.children[0])
                    if var_name not in self.variables:
                        undefined_vars.add(var_name)
                for child in node.children:
                    check_vars(child)
            else:
                # Only check if it's potentially a variable (alphanumeric)
                var_name = str(node)
                if var_name.isalnum() and not var_name.isdigit():
                    if var_name not in self.variables:
                        undefined_vars.add(var_name)
        
        check_vars(tree)
        return list(undefined_vars)
