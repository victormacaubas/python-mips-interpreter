import unittest
from src.lexer.lexer import Lexer, Token, TokenType
from src.errors.error_manager import ErrorManager

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.error_manager = ErrorManager()
        self.maxDiff = None

    def test_lexical_analysis(self):
        code = """
        add $t1, $t2, $t3
        lw $t0, 1000($t1)
        beq $t0, $t1, label
        label: addi $t0, $t1, 0010
        """
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        expected_tokens = [
            Token(TokenType.INSTRUCTION, 'add'),
            Token(TokenType.REGISTER, '$t1'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.REGISTER, '$t2'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.REGISTER, '$t3'),
            Token(TokenType.INSTRUCTION, 'lw'),
            Token(TokenType.REGISTER, '$t0'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IMMEDIATE, '1000'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.REGISTER, '$t1'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.INSTRUCTION, 'beq'),
            Token(TokenType.REGISTER, '$t0'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.REGISTER, '$t1'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.LABEL, 'label'),
            Token(TokenType.LABEL, 'label'),
            Token(TokenType.COLON, ':'),
            Token(TokenType.INSTRUCTION, 'addi'),
            Token(TokenType.REGISTER, '$t0'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.REGISTER, '$t1'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IMMEDIATE, '0010'),
            Token(TokenType.EOF, None)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_token(self):
        code = "add $t1, $t2, $t3!"
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        self.assertTrue(self.error_manager.has_errors())
        self.assertIn("LexicalError: Invalid token", self.error_manager.get_errors()[0])

    def test_empty_input(self):
        code = ""
        lexer = Lexer(code, self.error_manager)
        tokens = lexer.tokenize()
        expected_tokens = [Token(TokenType.EOF, None)]
        self.assertEqual(tokens, expected_tokens)
        self.assertFalse(self.error_manager.has_errors())

if __name__ == '__main__':
    unittest.main()
