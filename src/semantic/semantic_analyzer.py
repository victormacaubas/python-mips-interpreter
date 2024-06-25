from src.errors.error_manager import ErrorManager
from src.errors.exceptions import SemanticError

class SemanticAnalyzer:
    def __init__(self, parse_tree, error_manager):
        self.parse_tree = parse_tree
        self.error_manager = error_manager
        self.labels = set()
        self.used_labels = set()

    def analyze(self):
        for node in self.parse_tree:
            if node['type'] == 'label_decl':
                self.labels.add(node['label'])
            elif node['type'] == 'I_instruction' and 'label' in node:
                self.used_labels.add(node['label'])
        self.check_unused_labels()
        self.check_undeclared_labels()

    def check_unused_labels(self):
        for label in self.labels:
            if label not in self.used_labels:
                self.error_manager.report_error(SemanticError, f"Label '{label}' declared but not used")

    def check_undeclared_labels(self):
        for label in self.used_labels:
            if label not in self.labels:
                self.error_manager.report_error(SemanticError, f"Label '{label}' used but not declared")
