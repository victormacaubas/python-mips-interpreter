import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer.lexer import Lexer
from parser.parser import Parser
from errors.error_manager import ErrorManager
from semantic.semantic_analyzer import SemanticAnalyzer

def main():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sample_app.asm')
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r') as file:
        input_code = file.read()

    error_manager = ErrorManager()

    lexer = Lexer(input_code, error_manager)
    tokens = lexer.tokenize()

    print("Tokens:")
    for token in tokens:
        print(token)

    parser = Parser(tokens, error_manager)
    parse_tree = parser.parse()

    print("\nParse Tree:")
    for node in parse_tree:
        print(node)
        
    semantic_analyzer = SemanticAnalyzer(parse_tree, error_manager)
    semantic_analyzer.analyze()

    if error_manager.has_errors():
        print("\nErrors:")
        for error in error_manager.get_errors():
            print(error)
    else:
        print("\nNo errors found.")

if __name__ == "__main__":
    main()
