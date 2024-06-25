class TokenType:
    INSTRUCTION = 'INSTRUCTION'
    REGISTER = 'REGISTER'
    IMMEDIATE = 'IMMEDIATE'
    LABEL = 'LABEL'
    ADDRESS = 'ADDRESS'
    COMMA = 'COMMA'
    COLON = 'COLON'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value