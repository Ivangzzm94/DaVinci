import sys

class ErrorHandler(SyntaxError):
    def __init__(self, message):
        self.message = message
        self.error = 'Syntax error'

    def print(self, lineno):
        print('{} at line {}: {}'.format(self.error, lineno, self.message), file=sys.stderr)

    @staticmethod
    def redefined_function(message):
        e = ErrorHandler(message)
        e.error = 'Redefined function'
        return e

    @staticmethod
    def redefined_variable(message):
        e = ErrorHandler(message)
        e.error = 'Redefined variable'
        return e

    @staticmethod
    def undefined_variable(message):
        e = ErrorHandler(message)
        e.error = 'Undefined variable'
        return e

    @staticmethod
    def undefined_function(message):
        e = ErrorHandler(message)
        e.error = 'Undefined function'
        return e