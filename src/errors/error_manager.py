class ErrorManager:
    def __init__(self):
        self.errors = []

    def report_error(self, error_type, message, line=None, column=None):
        error_message = f"{error_type.__name__}: {message}"
        if line is not None and column is not None:
            error_message += f" at line {line}, column {column}"
        self.errors.append(error_message)
        print(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

    def clear_errors(self):
        self.errors = []
