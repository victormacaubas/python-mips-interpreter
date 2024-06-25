from src.lexer.lexer import Lexer
from src.lexer.token import Token, TokenType
from src.errors.error_manager import ErrorManager
from src.errors.exceptions import SyntaxError

class Parser:
    def __init__(self, tokens, error_manager):
        self.tokens = tokens
        self.pos = 0
        self.error_manager = error_manager

    def current_token(self):
        return self.tokens[self.pos]
    
    def consume_token(self, token_type):
        if self.current_token().type == token_type:
            self.pos += 1
        else:
            self.error(f"Expected token {token_type}, but got {self.current_token().type}")
    
    def parse(self):
        return self.parse_expression()
    
    def parse_expression(self):
        nodes = []

        while self.current_token().type != TokenType.EOF:
            if self.current_token().type == TokenType.LABEL:
                nodes.append(self.label_decl())
            else:
                nodes.append(self.instruction())
        return nodes
    
    def label_decl(self):
        label = self.current_token().value
        self.consume_token(TokenType.LABEL)
        self.consume_token(TokenType.COLON)
        return {
            'type': 'label_decl',
            'label': label
        }
    
    def instruction(self):
        if self.current_token().type == TokenType.INSTRUCTION:
            instruction = self.current_token().value
            self.consume_token(TokenType.INSTRUCTION)
            if instruction in ["add", "sub", "and", "or", "nor"]:
                return self.r_instruction(instruction)
            elif instruction in ["lw", "sw", "beq", "bne", "addi", "subi", "andi", "ori"]:
                return self.i_instruction(instruction)
            elif instruction == "j":
                return self.j_instruction(instruction)
            else:
                self.error_manager.report_error(SyntaxError, "Invalid instruction", line=self.pos)

    
    def r_instruction(self, instruction):
        reg1 = self.current_token().value
        self.consume_token(TokenType.REGISTER)
        self.consume_token(TokenType.COMMA)
        reg2 = self.current_token().value
        self.consume_token(TokenType.REGISTER)
        self.consume_token(TokenType.COMMA)
        reg3 = self.current_token().value
        self.consume_token(TokenType.REGISTER)

        return {
            "type": "R_instruction",
            "instruction": instruction,
            "reg1": reg1,
            "reg2": reg2,
            "reg3": reg3
        }

    def i_instruction(self, instruction):
        reg1 = self.current_token().value
        self.consume_token(TokenType.REGISTER)
        self.consume_token(TokenType.COMMA)
        if instruction in ["lw", "sw"]:
            address = self.address()

            return {
                "type": "I_instruction",
                "instruction": instruction,
                "reg1": reg1,
                "address": address
            }
        else:
            reg2 = self.current_token().value
            self.consume_token(TokenType.REGISTER)
            self.consume_token(TokenType.COMMA)

            if instruction in ["beq", "bne"]:
                label = self.current_token().value
                self.consume_token(TokenType.LABEL)

                return {
                    "type": "I_instruction",
                    "instruction": instruction,
                    "reg1": reg1,
                    "reg2": reg2,
                    "label": label
                }
            else:
                immediate = self.current_token().value
                self.consume_token(TokenType.IMMEDIATE)
                
                return {
                    "type": "I_instruction",
                    "instruction": instruction,
                    "reg1": reg1,
                    "reg2": reg2,
                    "immediate": immediate
                }

    def j_instruction(self, instruction):
        label = self.current_token().value
        self.consume_token(TokenType.LABEL)

        return {
            "type": "J_instruction",
            "instruction": instruction,
            "label": label
        }

    def address(self):
        immediate = self.current_token().value
        self.consume_token(TokenType.IMMEDIATE)
        self.consume_token(TokenType.LPAREN)
        reg = self.current_token().value
        self.consume_token(TokenType.REGISTER)
        self.consume_token(TokenType.RPAREN)

        return {
            "immediate": immediate,
            "register": reg
        }

    def error(self, message):
        self.error_manager.report_error(SyntaxError, message, line=self.pos)
