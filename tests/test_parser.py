import unittest
from src.parser.parser import Parser
from src.lexer.lexer import Lexer
from src.errors.error_manager import ErrorManager
from src.errors.exceptions import LexicalError, SyntaxError, SemanticError

class TestParser(unittest.TestCase):
    def setUp(self):
        self.error_manager = ErrorManager()

    def test_r_instruction(self):
        code = "add $t1, $t2, $t3"
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        parser = Parser(tokens, self.error_manager)
        result = parser.parse()
        expected = [
            {
                'type': 'R_instruction',
                'instruction': 'add',
                'reg1': '$t1',
                'reg2': '$t2',
                'reg3': '$t3'
            }
        ]
        self.assertEqual(result, expected)

    def test_i_instruction(self):
        code = "lw $t1, 1000($t2)"
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        parser = Parser(tokens, self.error_manager)
        result = parser.parse()
        expected = [
            {
                'type': 'I_instruction', 
                'instruction': 'lw',
                    'reg1': '$t1', 
                    'address': {'immediate': '1000', 'register': '$t2'}}
            ]
        self.assertEqual(result, expected)
    
    def test_j_instruction(self):
        code = "j label"
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        parser = Parser(tokens, self.error_manager)
        result = parser.parse()
        expected = [{'type': 'J_instruction', 'instruction': 'j', 'label': 'label'}]
        self.assertEqual(result, expected)

    def test_program(self):
        code = """
        label:
        add $t1, $t2, $t3
        lw $t1, 1000($t2)
        j label
        """
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        parser = Parser(tokens, self.error_manager)
        result = parser.parse()
        expected = [
            {'type': 'label_decl', 'label': 'label'},
            {'type': 'R_instruction', 'instruction': 'add', 'reg1': '$t1', 'reg2': '$t2', 'reg3': '$t3'},
            {'type': 'I_instruction', 'instruction': 'lw', 'reg1': '$t1', 'address': {'immediate': '1000', 'register': '$t2'}},
            {'type': 'J_instruction', 'instruction': 'j', 'label': 'label'}
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
