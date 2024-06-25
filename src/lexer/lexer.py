import re
from src.lexer.token import TokenType, Token
from src.errors.error_manager import ErrorManager
from src.errors.exceptions import LexicalError

class Lexer:
    def __init__(self, input_code, error_manager):
        self.input_code = input_code
        self.pos = 0
        self.tokens = []
        self.token_mapping = [
            (TokenType.INSTRUCTION, r'\b(?:add|sub|and|or|nor|lw|sw|beq|bne|j|addi|subi|andi|ori)\b'),
            (TokenType.REGISTER, r'\$(?:zero|t[0-9]|s[0-7]|a[0-3]|v[0-1]|gp|fp|ra|at)'),
            (TokenType.IMMEDIATE, r'\b\d+\b'),
            (TokenType.LABEL, r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
            (TokenType.COMMA, r','),
            (TokenType.COLON, r':'),
            (TokenType.LPAREN, r'\('),
            (TokenType.RPAREN, r'\)')
        ]
        self.error_manager = error_manager

    def tokenize(self):
        while self.pos < len(self.input_code):
            match = None
            if self.input_code[self.pos].isspace():
                self.pos += 1
                continue
            if self.input_code[self.pos] == '#':
                while self.pos < len(self.input_code) and self.input_code[self.pos] != '\n':
                    self.pos += 1
                continue

            for token_type, pattern in self.token_mapping:
                regex = re.compile(pattern)
                match = regex.match(self.input_code, self.pos)
                if match:
                    value = match.group(0)
                    self.tokens.append(Token(token_type, value))
                    self.pos = match.end()
                    break
            if not match:
                self.error_manager.report_error(LexicalError, "Invalid token", line=self.pos)
                self.pos += 1
        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens
