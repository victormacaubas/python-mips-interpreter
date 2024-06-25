class MIPSInterpreterError(Exception):
    """Base class for all errors types."""
    pass

class LexicalError(MIPSInterpreterError):
    """Exception for lexical analysis errors."""
    pass

class SyntaxError(MIPSInterpreterError):
    """Exception for syntax analysis errors."""
    pass

class SemanticError(MIPSInterpreterError):
    """Exception for semantic analysis errors."""
    pass
