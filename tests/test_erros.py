import unittest
from src.errors.error_manager import ErrorManager
from src.errors.exceptions import LexicalError, SyntaxError, SemanticError

class TestError(unittest.TestCase):

    def setUp(self):
        self.error_manager = ErrorManager()

    def test_report_lexical_error(self):
        self.error_manager.report_error(LexicalError, "Unexpected character", line=1, column=5)
        self.assertTrue(self.error_manager.has_errors())
        errors = self.error_manager.get_errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "LexicalError: Unexpected character at line 1, column 5")

    def test_report_syntax_error(self):
        self.error_manager.report_error(SyntaxError, "Unexpected token", line=2, column=10)
        self.assertTrue(self.error_manager.has_errors())
        errors = self.error_manager.get_errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "SyntaxError: Unexpected token at line 2, column 10")

    def test_report_semantic_error(self):
        self.error_manager.report_error(SemanticError, "Undeclared variable", line=3, column=15)
        self.assertTrue(self.error_manager.has_errors())
        errors = self.error_manager.get_errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "SemanticError: Undeclared variable at line 3, column 15")

    def test_clear_errors(self):
        self.error_manager.report_error(LexicalError, "Unexpected character", line=1, column=5)
        self.error_manager.clear_errors()
        self.assertFalse(self.error_manager.has_errors())
        self.assertEqual(len(self.error_manager.get_errors()), 0)

if __name__ == '__main__':
    unittest.main()
