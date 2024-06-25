import unittest
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.errors.error_manager import ErrorManager

class TestSemanticAnalyzer(unittest.TestCase):

    def setUp(self):
        self.error_manager = ErrorManager()
        self.maxDiff = None

    def analyze_code(self, code):
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        parser = Parser(tokens, self.error_manager)
        parse_tree = parser.parse()
        semantic_analyzer = SemanticAnalyzer(parse_tree, self.error_manager)
        semantic_analyzer.analyze()
        return self.error_manager.get_errors()

    def test_undeclared_label(self):
        code = """
        add $t1, $t2, $t3
        beq $t1, $t2, undeclared_label
        """
        errors = self.analyze_code(code)
        self.assertIn("SemanticError: Label 'undeclared_label' used but not declared", errors)

    def test_unused_label(self):
        code = """
        label: add $t1, $t2, $t3
        """
        errors = self.analyze_code(code)
        self.assertIn("SemanticError: Label 'label' declared but not used", errors)

    def test_correct_label_usage(self):
        code = """
        label: add $t1, $t2, $t3
        beq $t1, $t2, label
        """
        errors = self.analyze_code(code)
        self.assertFalse(errors)

if __name__ == '__main__':
    unittest.main()
