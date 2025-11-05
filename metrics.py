from lark import Tree
import time

class ParserMetrics:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all metrics"""
        self.parsing_time = 0
        self.tree_depth = 0
        self.node_count = 0
        self.operation_count = 0
        self.variable_count = 0
        self.number_count = 0

    def calculate_metrics(self, tree, parsing_duration):
        """Calculate metrics for a parsed tree"""
        self.reset()
        self.parsing_time = parsing_duration
        
        def analyze_node(node, depth=0):
            if isinstance(node, Tree):
                self.node_count += 1
                if node.data in ['add', 'mul']:
                    self.operation_count += 1
                
                current_depth = depth + 1
                self.tree_depth = max(self.tree_depth, current_depth)
                
                for child in node.children:
                    analyze_node(child, current_depth)
            else:
                # Leaf node
                try:
                    float(str(node))
                    self.number_count += 1
                except ValueError:
                    self.variable_count += 1

        analyze_node(tree)
        return self.get_metrics()

    def get_metrics(self):
        """Return all calculated metrics"""
        return {
            'parsing_time_ms': round(self.parsing_time * 1000, 2),
            'tree_depth': self.tree_depth,
            'total_nodes': self.node_count,
            'operations': self.operation_count,
            'variables': self.variable_count,
            'numbers': self.number_count,
            'complexity_score': self._calculate_complexity()
        }

    def _calculate_complexity(self):
        """Calculate a complexity score based on tree properties"""
        return round(
            (self.tree_depth * 0.4) +
            (self.operation_count * 0.3) +
            (self.variable_count * 0.2) +
            (self.number_count * 0.1),
            2
        )